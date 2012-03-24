# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import with_statement

from fabric import context_managers as fabric_ctx
from fudge import patch

from revolver import contextmanager as ctx
from revolver.core import env

def test_revolver_is_just_a_wrapper():
    assert ctx.cd == fabric_ctx.cd
    assert ctx.hide == fabric_ctx.hide
    assert ctx.lcd == fabric_ctx.lcd
    assert ctx.path == fabric_ctx.path
    assert ctx.prefix == fabric_ctx.prefix
    assert ctx.settings == fabric_ctx.settings
    assert ctx.show == fabric_ctx.show

def test_sudo_changes_env_flag():
    with ctx.sudo():
        assert env.sudo_forced

def test_sudo_without_user_does_not_change_sudo_env_user():
    old_user = env.sudo_user

    with ctx.sudo():
        assert env.sudo_user == old_user

def test_sudo_with_user_change_sudo_env_user():
    with ctx.sudo("foo"):
        assert env.sudo_user == "foo"

def test_sudo_restores_previous_settings():
    old_user = env.sudo_user
    old_forced = env.sudo_forced

    with ctx.sudo("foo"):
        pass

    assert env.sudo_forced == old_forced
    assert env.sudo_user == old_user

def test_sudo_default_login():
    old_shell = env.shell
    with ctx.sudo():
        assert env.shell == old_shell

@patch("revolver.user.shell")
def test_sudo_with_interactive_login(shell):
    shell.expects_call().with_args("foo").returns("bar")

    with ctx.sudo("foo", login=True):
        assert env.shell == "-i bar -i -c"
