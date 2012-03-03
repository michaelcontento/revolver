# -*- coding: utf-8 -*-

from __future__ import with_statement

from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import log
from revolver import user
from revolver.core import local, env

def inside():
    return dir.exists('/vagrant') and user.exists('vagrant')

def is_running():
    with ctx.settings(warn_only=True):
        command = "vagrant status | egrep -o 'running$'"
        vm_running = local(command, capture=True)

    if vm_running == None or vm_running == "":
        return False

    return True

def ip():
    # TODO: Use "vagrant ssh-config" instead 
    # TODO: Print proper error message if something went wrong
    command = "grep '^ *config.vm.network' Vagrantfile | egrep -o '[0-9\.]{7,}'"
    return local(command, capture=True)

def select():
    if not is_running():
        log.abort('Vagrant based VM currently NOT running')

    env.password = 'vagrant'
    env.hosts = ['vagrant@%s' % ip()]
