# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from fudge import patch
import cuisine

from revolver import server

from .utils import run_result


def test_revolver_is_just_a_wrapper():
    assert server.uuid == cuisine.system_uuid


@patch("revolver.file.copy")
def test_timezone_default(copy):
    copy.expects_call().with_args("/usr/share/zoneinfo/UTC", "/etc/localtime")
    server.timezone()


@patch("revolver.file.copy")
def test_timezone(copy):
    copy.expects_call().with_args("/usr/share/zoneinfo/FOO", "/etc/localtime")
    server.timezone("FOO")


@patch("revolver.core.run")
def test_version(run):
    (run.expects_call()
        .with_args("lsb_release --release --short")
        .returns(run_result("foo")))
    assert server.version() == "foo"


@patch("revolver.core.run")
def test_codename(run):
    (run.expects_call()
        .with_args("lsb_release --codename --short")
        .returns(run_result("foo")))
    assert server.codename() == "foo"
