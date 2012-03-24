# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

import sys

import cuisine
from fabric.api import run as _run
from fabric.api import sudo as _sudo
from fabric.api import local, get, env, put

from revolver.decorator import inject_use_sudo

VERSION = '0.0.4'

env.sudo_forced = False
env.sudo_user = None

put = inject_use_sudo(put)

def run(*args, **kwargs):
    if not env.sudo_forced:
        return _run(*args, **kwargs)

    return sudo(*args, **kwargs)

def sudo(*args, **kwargs):
    if env.sudo_user:
        kwargs['user'] = env.sudo_user

    return _sudo(*args, **kwargs)

# Monkeypatch sudo/run into fabric/cuisine
for module in ("fabric.api", "fabric.operations", "cuisine"):
    setattr(sys.modules[module], "run", run)
    setattr(sys.modules[module], "sudo", sudo)
