# -*- coding: utf-8 -*-

from __future__ import with_statement

from datetime import datetime
import os

from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import file
from revolver import git
from revolver import log
from revolver import user
from revolver.core import put, run, sudo, local

def deploy(owner, upload_hook=None, revision='HEAD', keep_versions=10):
    if not user.exists(owner):
        log.abort('Specified owner does not exists! Deploy aborted')

    # Ensure some directories
    paths = _ensure_layout(owner)
    new_release_dir = _create_new_release_dir(owner, paths['releases'])
    paths['new_release'] = new_release_dir

    # Upload the new version and call the after upload hook
    _upload(owner, new_release_dir, revision)
    if upload_hook:
        with ctx.sudo(owner), ctx.cd(new_release_dir):
            upload_hook(owner, paths)

    # Activate the new release and 
    _symlink_release(owner, paths['current'], new_release_dir)
    _clear_old_releases(paths['releases'], keep_versions)

    return paths

def _ensure_layout(owner):
    home_dir = user.home_directory(owner)
    repo_name = git.repository_name()

    join = os.path.join
    project_dir = join(home_dir, repo_name)

    paths = {
        'project':  join(project_dir),
        'current':  join(project_dir, 'current'),
        'releases': join(project_dir, 'releases'), 
        'shared':   join(project_dir, 'shared'),
        'logs':     join(project_dir, 'shared', 'logs'),
        'temp':     join(project_dir, 'shared', 'temp')
    }

    with ctx.sudo(owner):
        for path in paths.itervalues():
            if dir.exists(path): 
                continue
            dir.create(path, recursive=True)

    return paths

def _create_new_release_dir(owner, base_dir):
    date_dir = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    release_dir = os.path.join(base_dir, date_dir)

    with ctx.sudo(owner):
        dir.create(release_dir)

    return release_dir

def _upload(owner, upload_dir, revision):
    tmp_tar = git.create_archive(revision)

    try:
        with ctx.cd(upload_dir):
            with ctx.sudo():
                put(tmp_tar, 'deploy.tar.gz')
                file.attributes('deploy.tar.gz', owner=owner)

            with ctx.sudo(owner):
                run('tar -xzf deploy.tar.gz')
                file.remove('deploy.tar.gz')
                file.write('VERSION', git.revparse(revision))
    finally:
        local('rm -rf %s' % tmp_tar)

def _symlink_release(owner, current_dir, release_dir):
    with ctx.sudo(owner):
        if dir.exists(current_dir):
            dir.remove(current_dir, recursive=True)
        file.link(release_dir, current_dir)

def _clear_old_releases(directory, keep):
    with ctx.cd(directory):
        sudo(
            'ls -1 | sort -V | head -n-%s | xargs -l1 rm -rf'
            % keep
        )
