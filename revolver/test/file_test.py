# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, with_statement

from fudge import patch
import cuisine
import fabric
from fabric.contrib import files as fabric_files

from revolver import file

from .utils import assert_contain_function_wrapped, run_result


def test_revolver_is_just_a_wrapper():
    assert file.attributes == cuisine.file_attribs
    assert file.attributes_get == cuisine.file_attribs_get
    assert file.ensure == cuisine.file_ensure
    assert file.exists == cuisine.file_is_file
    assert file.is_link == cuisine.file_is_link
    assert file.link == cuisine.file_link
    assert file.read == cuisine.file_read
    assert file.read_local == cuisine.file_local_read
    assert file.update == cuisine.file_update

    assert_contain_function_wrapped(file.append, fabric_files.append)
    assert_contain_function_wrapped(file.comment, fabric_files.comment)
    assert_contain_function_wrapped(file.contains, fabric_files.contains)
    assert_contain_function_wrapped(file.sed, fabric_files.sed)
    assert_contain_function_wrapped(file.uncomment, fabric_files.uncomment)
    assert_contain_function_wrapped(file.write, cuisine.file_write)


@patch("revolver.core.run")
@patch("revolver.file.attributes")
def test_temp_calles_mktemp(run, attributes):
    (run.expects_call()
        .with_args("mktemp")
        .returns(run_result("foo")))
    attributes.expects_call()
    assert file.temp() == "foo"


@patch("revolver.core.run")
@patch("revolver.file.attributes")
def test_temp_default_attributes(run, attributes):
    run.expects_call().returns(run_result("path"))
    (attributes.expects_call()
        .with_args("path", mode=None, owner=None, group=None))
    file.temp()


@patch("revolver.core.run")
@patch("revolver.file.attributes")
def test_temp_passes_attributes(run, attributes):
    run.expects_call().returns(run_result("path"))
    (attributes.expects_call()
        .with_args("path", mode="foo", owner="bar", group="baz"))
    file.temp("foo", "bar", "baz")


@patch("revolver.core.run")
def test_touch(run):
    run.expects_call().with_args("touch path")
    file.touch("path")


@patch("revolver.core.run")
@patch("revolver.file.attributes")
def test_touch_default_attributes(run, attributes):
    run.expects_call().returns(run_result("path"))
    (attributes.expects_call()
        .with_args("path", mode=None, owner=None, group=None))
    file.touch("path")


@patch("revolver.core.run")
@patch("revolver.file.attributes")
def test_touch_passes_attributes(run, attributes):
    run.expects_call().returns(run_result("path"))
    (attributes.expects_call()
        .with_args("path", mode="foo", owner="bar", group="baz"))
    file.touch("path", "foo", "bar", "baz")


@patch("revolver.core.run")
def test_remove_defaults(run):
    run.expects_call().with_args("rm -f  path")
    file.remove("path")


@patch("revolver.core.run")
def test_remove_recusrive(run):
    run.expects_call().with_args("rm -f  path")
    file.remove("path", recursive=False)

    run.expects_call().with_args("rm -f -r path")
    file.remove("path", recursive=True)


@patch("revolver.core.run")
def test_remove_force(run):
    run.expects_call().with_args("rm   path")
    file.remove("path", force=False)

    run.expects_call().with_args("rm -f  path")
    file.remove("path", force=True)


@patch("revolver.core.run")
def test_copy(run):
    run.expects_call().with_args("cp -f src dst")
    file.copy("src", "dst")


@patch("revolver.core.run")
def test_copy_force_false(run):
    run.expects_call().with_args("cp  src dst")
    file.copy("src", "dst", force=False)


@patch("revolver.core.run")
@patch("revolver.file.attributes")
def test_copy_default_attributes(run, attributes):
    run.expects_call()
    (attributes.expects_call()
        .with_args("dst", mode=None, owner=None, group=None))
    file.copy("src", "dst")


@patch("revolver.core.run")
@patch("revolver.file.attributes")
def test_copy_default_attributes(run, attributes):
    run.expects_call()
    (attributes.expects_call()
        .with_args("dst", mode="foo", owner="bar", group="baz"))
    file.copy("src", "dst", mode="foo", owner="bar", group="baz")
