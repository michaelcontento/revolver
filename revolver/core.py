# -*- coding: utf-8 -*-

from fabric import api as _fabric
from fabric.api import local, get, env, put
import cuisine as _cuisine

from revolver.decorator import inject_use_sudo

VERSION = '0.0.4'

env.sudo_forced = False
env.sudo_user = None

_run = _fabric.run
_sudo = _fabric.sudo
put = inject_use_sudo(put)

def run(*args, **kwargs):
    if not env.sudo_forced:
        return _run(*args, **kwargs)

    return sudo(*args, **kwargs)


def sudo(*args, **kwargs):
    if env.sudo_user:
        kwargs['user'] = env.sudo_user

    return _sudo(*args, **kwargs)

_fabric.run = _cuisine.run = run
_fabric.sudo = _cuisine.sudo = sudo
