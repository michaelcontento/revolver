# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from datetime import datetime
import posixpath

from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import file, git, core, command


class Deployinator(object):
    def __init__(self, cwd=None, name=None):
        self.cwd = cwd or core.run("pwd").stdout
        self.name = name or git.repository_name()
        self.releases_to_keep = 15
        self.revision = "HEAD"
        self._hooks = []
        self._init_folders()

    def add_hook(self, hook):
        self._hooks.append(hook(self))

    def dispatch_hook(self, name):
        for hook in self._hooks:
            method = getattr(hook, "on_%s" % name)
            if method:
                method()

    def run(self):
        self.dispatch_hook("before_layout")
        try:
            self._layout()
            self.dispatch_hook("after_layout")

            self.dispatch_hook("before_upload")
            self._upload()
            self.dispatch_hook("after_upload")

            self.dispatch_hook("before_cleanup")
            self._cleanup()
            self.dispatch_hook("after_cleanup")

            self.dispatch_hook("before_activate")
            self._activate()
        except:
            dir.remove(self.folders["releases.current"], recursive=True)
            raise
        self.dispatch_hook("after_activate")

    def _init_folders(self):
        project = posixpath.join(self.cwd, self.name)
        deploy = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

        join = posixpath.join
        self.folders = {
            "project": project,
            "current": join(project, "current"),
            "releases": join(project, "releases"),
            "releases.current": join(project, "releases", deploy),
            "shared": join(project, "shared"),
            "shared.logs": join(project, "shared", "logs"),
            "shared.temp": join(project, "shared", "temp"),
            "shared.run": join(project, "shared", "run")
        }

    def _layout(self):
        current_user = core.run("echo $USER").stdout

        for type, path in self.folders.iteritems():
            if not dir.exists(path):
                if type != "current":
                    dir.create(path, recursive=True)
            else:
                dir.attributes(path, owner=current_user, recursive=True)

    def _upload(self):
        # TODO Warn if there are local changes
        tmp_tar = git.create_archive(self.revision)

        try:
            with ctx.cd(self.folders["releases.current"]):
                core.put(tmp_tar, "deploy.tar.gz")
                core.run("tar -xzf deploy.tar.gz")
                file.remove("deploy.tar.gz")

                # TODO Fix file.write(). Sometimes the temp-file workaround of
                #      Fabric seems to be broken. Uncomment the following line
                #      after everything is fixed.
                # file.write("VERSION", git.revparse(self.revision))
        finally:
            core.local("rm -rf %s" % tmp_tar)

    def _cleanup(self):
        with ctx.cd(self.folders["releases"]):
            core.run("ls -1 | sort -V | head -n-%s | xargs -l1 rm -rf"
                % self.releases_to_keep)

    def _activate(self):
        file.link(self.folders["releases.current"], self.folders["current"])


class BaseHook(object):
    def __init__(self, deployinator):
        self.deployinator = deployinator

    def __getattr__(self, name):
        if name.startswith("on_"):
            return None
        return getattr(self.deployinator, name)


class AutoDependencyHook(BaseHook):
    def on_after_upload(self):
        self.dispatch_hook("before_dependencies")
        self._dependencies()
        self.dispatch_hook("after_dependencies")

    def _dependencies(self):
        with ctx.cd(self.folders["releases.current"]):
            if file.exists("package.json"):
                self._dependencies_package_json()

            if file.exists("Gemfile"):
                self._dependencies_gemfile()

            if file.exists("setup.py"):
                self._dependencies_setup_py()

            if file.exists("requirements.txt"):
                self._dependencies_requirements_txt()

    def _dependencies_package_json(self):
        if command.exists("npm"):
            core.run("npm install")

    def _dependencies_gemfile(self):
        if command.exists("bundle"):
            core.run("bundle")

    def _dependencies_setup_py(self):
        # TODO Implement setup.py resolution
        pass

    def _dependencies_requirements_txt(self):
        if command.exists("pip"):
            core.run("pip install -r requirements.txt --use-mirrors")
