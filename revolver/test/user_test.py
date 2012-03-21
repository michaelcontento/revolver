# -*- coding: utf-8 -*-

from cuisine import user_check as cuisine_get
from cuisine import user_create as cuisine_create
from cuisine import user_ensure as cuisine_ensure
from cuisine import user_remove as cuisine_remove
from fudge import patch

from revolver import user

def test_revolver_is_just_a_wrapper():
    assert user.get == cuisine_get
    assert user.create == cuisine_create
    assert user.ensure == cuisine_ensure
    assert user.remove == cuisine_remove

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
