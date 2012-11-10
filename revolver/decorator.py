# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from functools import wraps

from fabric.decorators import (task, hosts, roles, runs_once, serial,
                               parallel, with_settings)
from fabric.network import needs_host

from revolver.core import env
from revolver import contextmanager as ctx


def sudo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with ctx.sudo():
            func(*args, **kwargs)
    return wrapper


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
        func_args = func.func_code.co_varnames[:func.func_code.co_argcount]

        # Fabric
        if "use_sudo" not in kwargs and "use_sudo" in func_args:
            kwargs["use_sudo"] = env.sudo_forced

        # Cuisine
        if "sudo" not in kwargs and "sudo" in func_args:
            kwargs["sudo"] = env.sudo_forced

        return func(*args, **kwargs)
    return inject_wrapper
