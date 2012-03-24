# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from fudge import patch

from revolver import vagrant, core

@patch("revolver.directory.exists", "revolver.user.exists")
def test_inside_arguments(dir_exists, user_exists):
    dir_exists.expects_call().with_args("/vagrant").returns(True)
    user_exists.expects_call().with_args("vagrant")
    vagrant.inside()

@patch("revolver.directory.exists", "revolver.user.exists")
def test_inside(dir_exists, user_exists):
    dir_exists.expects_call().returns(True)
    user_exists.expects_call().returns(True)
    assert vagrant.inside()

@patch("revolver.directory.exists")
def test_not_inside_if_dir_is_missing(dir_exists):
    dir_exists.expects_call().returns(False)
    assert not vagrant.inside()

@patch("revolver.directory.exists", "revolver.user.exists")
def test_not_inside_if_dir_is_missing(dir_exists, user_exists):
    dir_exists.expects_call().returns(True)
    user_exists.expects_call().returns(False)
    assert not vagrant.inside()

@patch("revolver.core.local")
def test_is_running_arguments(local):
    command = "vagrant status | egrep -o 'running$'"
    local.expects_call().with_args(command, capture=True)
    vagrant.is_running()

@patch("revolver.core.local")
def test_is_not_running_if_result_is_none(local):
    local.expects_call().returns(None)
    assert not vagrant.is_running()

@patch("revolver.core.local")
def test_is_not_running_if_result_is_blank(local):
    local.expects_call().returns("")
    assert not vagrant.is_running()

@patch("revolver.core.local")
def test_is_running(local):
    local.expects_call().returns("some non empty string")
    assert vagrant.is_running()

@patch("revolver.vagrant.is_running", "revolver.log.abort")
def test_select_aborts_if_not_running(is_running, abort):
    is_running.expects_call().returns(False)
    abort.expects_call().with_args("Vagrant based VM currently NOT running")
    vagrant.select()

@patch("revolver.vagrant.is_running")
@patch("revolver.directory.temp_local")
@patch("revolver.core.local")
def test_select_changes_the_environment(is_running, temp_local, local):
    is_running.expects_call().returns(True)
    temp_local.expects_call().returns("/tmp")
    local.expects_call().with_args("vagrant ssh-config > /tmp/vagrant_ssh_config")
    vagrant.select()

    assert core.env.hosts == ["default"]
    assert core.env.password == "vagrant"
    assert core.env.ssh_config_path == "/tmp/vagrant_ssh_config"
    assert core.env.use_ssh_config
