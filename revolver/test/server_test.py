# -*- coding: utf-8 -*-

from cuisine import system_uuid as cuisine_uuid
from fudge import patch

from revolver import server

def test_revolver_is_just_a_wrapper():
    assert server.uuid == cuisine_uuid

@patch("revolver.file.copy")
def test_timezone_default(copy):
    copy.expects_call().with_args("/usr/share/zoneinfo/UTC", "/etc/localtime")
    server.timezone()

@patch("revolver.file.copy")
def test_timezone(copy):
    copy.expects_call().with_args("/usr/share/zoneinfo/FOO", "/etc/localtime")
    server.timezone("FOO")

@patch("revolver.core._run")
def test_version(run):
    run.expects_call().with_args("lsb_release --release --short").returns("foo")
    assert server.version() == "foo"

@patch("revolver.core._run")
def test_codename(run):
    run.expects_call().with_args("lsb_release --codename --short").returns("foo")
    assert server.codename() == "foo"
