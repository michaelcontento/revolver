# -*- coding: utf-8 -*-

from cuisine import package_ensure as cuisine_ensure
from cuisine import package_install as cuisine_install
from cuisine import package_update as cuisine_update
from cuisine import package_upgrade as cuisine_upgrade
from fudge import patch

from revolver import package

from .utils import assert_contain_function_wrapped

def test_revolver_is_just_a_wrapper():
    assert package.upgrade == cuisine_upgrade

    assert_contain_function_wrapped(package.ensure, cuisine_ensure)
    assert_contain_function_wrapped(package.install, cuisine_install)
    assert_contain_function_wrapped(package.update, cuisine_update)

@patch("revolver.core._run")
def test_is_installed(run):
    (run.expects_call()
        .with_args("dpkg -s foo")
        .returns("Status: foo installed"))
    assert package.is_installed("foo")

@patch("revolver.core._run")
def test_is_not_installed_without_status(run):
    (run.expects_call()
        .with_args("dpkg -s foo")
        .returns("foo installed"))
    assert not package.is_installed("foo")

@patch("revolver.package.ensure")
@patch("revolver.server.codename")
@patch("revolver.file.exists")
@patch("revolver.core._sudo")
@patch("revolver.package.update")
def test_install_ppa(ensure, codename, exists, sudo, update):
    ensure.expects_call().with_args("python-software-properties")
    codename.expects_call().returns("bar")
    exists.expects_call().with_args("foo-bar.list").returns(False)
    sudo.expects_call().with_args("add-apt-repository ppa:foo")
    update.expects_call()
    package.install_ppa("foo")

@patch("revolver.package.ensure")
@patch("revolver.server.codename")
@patch("revolver.file.exists")
def test_install_ppa_if_ppa_exists(ensure, codename, exists):
    ensure.expects_call().with_args("python-software-properties")
    codename.expects_call().returns("bar")
    exists.expects_call().with_args("foo-bar.list").returns(True)
    package.install_ppa("foo")

@patch("revolver.package.ensure")
@patch("revolver.server.codename")
@patch("revolver.file.exists")
def test_install_ppa_normalize_path(ensure, codename, exists):
    ensure.expects_call().with_args("python-software-properties")
    codename.expects_call().returns("bar")
    exists.expects_call().with_args("foo-baz-bar.list").returns(True)
    package.install_ppa("foo/baz")
