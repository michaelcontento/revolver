# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from fudge import patch
import cuisine
import fabric

from revolver import core

from .utils import assert_contain_function_wrapped


def test_revolver_is_just_a_wrapper():
    assert core.env == fabric.api.env
    assert core.get == fabric.api.get
    assert core.local == fabric.api.local


def test_environment_default_values():
    assert not core.env.sudo_forced
    assert core.env.sudo_user is None


def test_patch_fabric_api():
    assert fabric.api.run == core.run
    assert fabric.api.sudo == core.sudo


def test_patch_fabric_operations():
    assert fabric.operations.run == core.run
    assert fabric.operations.sudo == core.sudo


def test_patch_cuisine():
    assert cuisine.run == core.run
    assert cuisine.sudo == core.sudo


def test_original_methods_are_available_but_private():
    assert core._run.__module__ == "fabric.operations"
    assert core._sudo.__module__ == "fabric.operations"


@patch("revolver.core.sudo")
def test_force_sudo_via_env(sudo):
    sudo.expects_call().with_args("foo")
    core.env.sudo_forced = True
    core.run("foo")
    core.env.sudo_forced = False


@patch("revolver.core._sudo")
def test_inject_user_for_sudo_via_env(_sudo):
    _sudo.expects_call().with_args("foo", user="bar")
    core.env.sudo_user = "bar"
    core.sudo("foo")
    core.env.sudo_user = None


@patch("revolver.core._put")
def test_put_does_not_pass_any_default_args(_put):
    _put.expects_call().with_args()
    core.put()


@patch("revolver.core._put")
def test_put_passes_any_given_args(_put):
    _put.expects_call().with_args("foo", baz="bar")
    core.put("foo", baz="bar")
