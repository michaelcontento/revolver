# -*- coding: utf-8 -*-

from contextlib import contextmanager

from fabric.context_managers import cd
from fabric.context_managers import hide
from fabric.context_managers import lcd
from fabric.context_managers import path
from fabric.context_managers import prefix
from fabric.context_managers import settings
from fabric.context_managers import show

from revolver.core import env

@contextmanager
def sudo(user=None):
    old_forced = env.sudo_forced
    env.sudo_forced = True

    old_user = env.sudo_user
    env.sudo_user = user

    yield

    env.sudo_forced = old_forced
    env.sudo_user = old_user
