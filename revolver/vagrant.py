# -*- coding: utf-8 -*-

from __future__ import with_statement

import os

from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import log
from revolver import user
from revolver.core import local, env

def inside():
    return dir.exists("/vagrant") and user.exists("vagrant")

def is_running():
    with ctx.settings(warn_only=True):
        command = "vagrant status | egrep -o 'running$'"
        vm_running = local(command, capture=True)

    if vm_running == None or vm_running == "":
        return False

    return True

def select():
    if not is_running():
        log.abort("Vagrant based VM currently NOT running")
    
    config_path = os.path.join(dir.temp_local(), "vagrant_ssh_config")
    local("vagrant ssh-config > %s" % config_path)

    env.hosts = ["default"]
    env.password = "vagrant"
    env.ssh_config_path = config_path 
    env.use_ssh_config = True
