# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from fudge import patch
import fabric

from revolver import service


@patch("revolver.core.sudo")
def test_is_running(sudo):
    command = "/etc/init.d/foo status"
    result = fabric.operations._AttributeList("")
    result.succeeded = "succeeded"

    sudo.expects_call().with_args(command).returns(result)
    assert service.is_running("foo") == "succeeded"


@patch("revolver.core.sudo")
@patch("revolver.file.exists")
def test_command(sudo, exists):
    exists.expects_call().returns(False).next_call().returns(True)
    sudo.expects_call().with_args("/etc/init.d/foo method")
    service.command("foo", "method")


@patch("revolver.core.sudo")
@patch("revolver.file.exists")
def test_command_upstart(sudo, exists):
    exists.expects_call().with_args("/etc/init/foo.conf").returns(True)
    sudo.expects_call().with_args("method foo")
    service.command("foo", "method")


@patch("revolver.core.sudo")
@patch("revolver.file.exists")
def test_command_initd(sudo, exists):
    (exists
        .expects_call()
            .returns(False)
        .next_call()
            .with_args("/etc/init.d/foo")
            .returns(True))
    sudo.expects_call().with_args("/etc/init.d/foo method")
    service.command("foo", "method")


@patch("revolver.service.command")
def test_start(command):
    command.expects_call().with_args("foo", "start")
    service.start("foo")


@patch("revolver.service.command")
def test_stop(command):
    command.expects_call().with_args("foo", "stop")
    service.stop("foo")


@patch("revolver.service.command")
def test_restart(command):
    command.expects_call().with_args("foo", "restart")
    service.restart("foo")


@patch("revolver.service.command")
def test_reload(command):
    command.expects_call().with_args("foo", "reload")
    service.reload("foo")
