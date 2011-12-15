# -*- coding: utf-8 -*-

from cuisine import package_ensure as ensure
from cuisine import package_install as install
from cuisine import package_update as update

from revolver import contextmanager as ctx
from revolver import file
from revolver import server
from revolver.core import sudo, run

def is_installed(name):
    with ctx.settings(warn_only=True):
        res = run("dpkg -s %s" % name)
        for line in res.splitlines():
            if line.startswith("Status: "):
                status = line[8:]
                if "installed" in status.split(' '):
                    return True
        return False

def install_ppa(name):
    ensure('python-software-properties')

    with ctx.cd('/etc/apt/sources.list.d'):
        name_normalizes = name.replace('/', '-')
        source_list = '%s-%s.list' % (name_normalizes, server.codename())

        if not file.exists(source_list):
            sudo('add-apt-repository ppa:%s' % name)
            update()
