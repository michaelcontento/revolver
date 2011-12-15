# -*- coding: utf-8 -*-

from functools import wraps

from cuisine import multiargs
from fabric.decorators import task, hosts, roles, runs_once, serial, parallel, with_settings
from fabric.network import needs_host

from revolver.core import env

def inject_use_sudo(func):
    @wraps(func)
    def inject_wrapper(*args, **kwargs):
        if not 'use_sudo' in kwargs:
            kwargs['use_sudo'] = env.sudo_forced
        return func(*args, **kwargs)
    return inject_wrapper
