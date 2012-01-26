# -*- coding: utf-8 -*-

from fabric import context_managers as old_ctx

from revolver import contextmanager as new_ctx
from revolver.core import env

def test_revolver_is_just_a_wrapper():
    assert new_ctx.cd == old_ctx.cd
    assert new_ctx.hide == old_ctx.hide
    assert new_ctx.lcd == old_ctx.lcd
    assert new_ctx.path == old_ctx.path
    assert new_ctx.prefix == old_ctx.prefix
    assert new_ctx.settings == old_ctx.settings
    assert new_ctx.show == old_ctx.show

def test_sudo_changes_env_flag():
    with new_ctx.sudo():
        assert env.sudo_forced
    
def test_sudo_without_user_does_not_change_sudo_env_user():
    with new_ctx.sudo():
        assert env.sudo_user == None

def test_sudo_with_user_change_sudo_env_user():
    with new_ctx.sudo("foo"):
        assert env.sudo_user == "foo"

def test_sudo_restores_previous_settings():
    with new_ctx.sudo("foo"):
        pass

    assert not env.sudo_forced
    assert env.sudo_user == None 
