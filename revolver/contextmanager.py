# -*- coding: utf-8 -*-

from __future__ import with_statement

from contextlib import contextmanager

from fabric.context_managers import cd
from fabric.context_managers import hide
from fabric.context_managers import lcd
from fabric.context_managers import path
from fabric.context_managers import prefix
from fabric.context_managers import settings
from fabric.context_managers import show

from revolver import user
from revolver.core import env

@contextmanager
def sudo(username=None, login=False):
    old_forced = env.sudo_forced
    old_user = env.sudo_user
    old_shell = env.shell

    env.sudo_forced = True
    env.sudo_user = username

    if login:
        with sudo():
            user_shell = user.shell(username) 
        env.shell = "-i %s -i -c" % user_shell

    yield

    env.sudo_forced = old_forced
    env.sudo_user = old_user
    env.shell = old_shell
