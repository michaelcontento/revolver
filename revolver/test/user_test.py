# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from fudge import patch
import cuisine

from revolver import user

def test_revolver_is_just_a_wrapper():
    assert user.get == cuisine.user_check
    assert user.create == cuisine.user_create
    assert user.ensure == cuisine.user_ensure
    assert user.remove == cuisine.user_remove

@patch("revolver.user.get")
def test_exists(get):
    get.expects_call().with_args("user").returns(None)
    assert not user.exists("user")

    get.expects_call().with_args("user").returns({})
    assert user.exists("user")

@patch("revolver.user.get")
def test_shell(get):
    get.expects_call().with_args("user").returns({"shell": "bar"})
    assert user.shell("user") == "bar"

@patch("revolver.user.get")
@patch("revolver.log.abort")
def test_shell_abort_on_error(get, abort):
    get.expects_call().with_args("user").returns(None)
    abort.expects_call().with_args("user 'user' does not exists")
    assert not user.shell("user")

@patch("revolver.user.get")
def test_home_directory(get):
    get.expects_call().with_args("user").returns({"home": "bar"})
    assert user.home_directory("user") == "bar"

@patch("revolver.user.get")
@patch("revolver.log.abort")
def test_home_directory_abort_on_error(get, abort):
    get.expects_call().with_args("user").returns(None)
    abort.expects_call().with_args("user 'user' does not exists")
    assert not user.home_directory("user")
