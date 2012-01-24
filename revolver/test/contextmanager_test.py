# -*- coding: utf-8 -*-

from fabric import context_managers as old_ctx

from revolver import contextmanager as new_ctx

def test_revolver_is_just_a_wrapper():
    assert new_ctx.cd == old_ctx.cd
    assert new_ctx.hide == old_ctx.hide
    assert new_ctx.lcd == old_ctx.lcd
    assert new_ctx.path == old_ctx.path
    assert new_ctx.prefix == old_ctx.prefix
    assert new_ctx.settings == old_ctx.settings
    assert new_ctx.show == old_ctx.show
