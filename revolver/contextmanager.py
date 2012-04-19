# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from contextlib import contextmanager

from fabric.context_managers import cd, hide, lcd, path, prefix, settings, show

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


@contextmanager
def unpatched_state():
    old_shell = env.shell
    old_sudo_forced = env.sudo_forced
    old_sudo_user = env.sudo_user

    env.shell = "/bin/bash -l -c"
    env.sudo_forced = False
    env.sudo_user = None

    yield

    env.shell = old_shell
    env.sudo_forced = old_sudo_forced
    env.sudo_user = old_sudo_user
