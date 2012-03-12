# -*- coding: utf-8 -*-

from functools import wraps

from fabric.decorators import task, hosts, roles, runs_once, serial, parallel, with_settings
from fabric.network import needs_host

from revolver.core import env

def multiargs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) == 0:
            return func()
        arg = args[0]
        args = args[1:]
        if type(arg) in (tuple, list):
            return map(lambda _: func(_, *args, **kwargs), arg)
        else:
            return func(arg, *args, **kwargs)
    return wrapper

def inject_use_sudo(func):
    @wraps(func)
    def inject_wrapper(*args, **kwargs):
        if not 'use_sudo' in kwargs:
            kwargs['use_sudo'] = env.sudo_forced
        return func(*args, **kwargs)
    return inject_wrapper
