# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from fudge import patch
import cuisine

from revolver import package, decorator

from .utils import assert_contain_function_wrapped


def test_revolver_is_just_a_wrapper():
    # TODO Check the decorator stack (multiargs and sudo)
    assert_contain_function_wrapped(package.ensure, cuisine.package_ensure)
    assert_contain_function_wrapped(package.install, cuisine.package_install)
    assert_contain_function_wrapped(package.update, cuisine.package_update)
    assert_contain_function_wrapped(package.upgrade, cuisine.package_upgrade)


@patch("revolver.core.run")
def test_is_installed(run):
    (run.expects_call()
        .with_args("dpkg -s foo")
        .returns("Status: foo installed"))
    assert package.is_installed("foo")


@patch("revolver.core.run")
def test_is_not_installed_without_status(run):
    (run.expects_call()
        .with_args("dpkg -s foo")
        .returns("foo installed"))
    assert not package.is_installed("foo")


@patch("revolver.package.ensure")
@patch("revolver.server.codename")
@patch("revolver.file.exists")
@patch("revolver.core.sudo")
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
