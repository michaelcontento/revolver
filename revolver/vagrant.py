# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

import os

from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import log, user, core

def inside():
    return dir.exists("/vagrant") and user.exists("vagrant")

def is_running():
    with ctx.settings(warn_only=True):
        command = "vagrant status | egrep -o 'running$'"
        vm_running = core.local(command, capture=True)

    if vm_running == None or vm_running == "":
        return False

    return True

def select():
    if not is_running():
        log.abort("Vagrant based VM currently NOT running")
        return

    config_path = os.path.join(dir.temp_local(), "vagrant_ssh_config")
    core.local("vagrant ssh-config > %s" % config_path)

    core.env.hosts = ["default"]
    core.env.password = "vagrant"
    core.env.ssh_config_path = config_path
    core.env.use_ssh_config = True
