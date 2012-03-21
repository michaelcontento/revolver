# -*- coding: utf-8 -*-

from cuisine import file_attribs as cuisine_attributes
from cuisine import file_attribs_get as cuisine_attributes_get
from cuisine import file_ensure as cuisine_ensure
from cuisine import file_is_file as cuisine_is_file
from cuisine import file_is_link as cuisine_is_link
from cuisine import file_link as cuisine_link
from cuisine import file_local_read as cuisine_read_local
from cuisine import file_read as cuisine_read
from cuisine import file_update as cuisine_update
from cuisine import file_write as cuisine_write
from fabric.contrib.files import append as fabric_append
from fabric.contrib.files import comment as fabric_comment
from fabric.contrib.files import contains as fabric_contains
from fabric.contrib.files import sed as fabric_sed
from fabric.contrib.files import uncomment as fabric_uncomment
from fudge import patch

from revolver import file

from .utils import assert_contain_function_wrapped

def test_revolver_is_just_a_wrapper():
    assert file.attributes == cuisine_attributes
    assert file.attributes_get == cuisine_attributes_get
    assert file.ensure == cuisine_ensure
    assert file.exists == cuisine_is_file
    assert file.is_link == cuisine_is_link
    assert file.link == cuisine_link
    assert file.read == cuisine_read
    assert file.read_local == cuisine_read_local
    assert file.update == cuisine_update

    assert_contain_function_wrapped(file.append, fabric_append)
    assert_contain_function_wrapped(file.comment, fabric_comment)
    assert_contain_function_wrapped(file.contains, fabric_contains)
    assert_contain_function_wrapped(file.sed, fabric_sed)
    assert_contain_function_wrapped(file.uncomment, fabric_uncomment)
    assert_contain_function_wrapped(file.write, cuisine_write)

@patch("revolver.core._run")
def test_touch(run):
    run.expects_call().with_args("touch path")
    file.touch("path")

@patch("revolver.core._run")
def test_remove_defaults(run):
    run.expects_call().with_args("rm -f  path")
    file.remove("path")

@patch("revolver.core._run")
def test_remove_recusrive(run):
    run.expects_call().with_args("rm -f  path")
    file.remove("path", recursive=False)

    run.expects_call().with_args("rm -f -r path")
    file.remove("path", recursive=True)

@patch("revolver.core._run")
def test_remove_force(run):
    run.expects_call().with_args("rm   path")
    file.remove("path", force=False)

    run.expects_call().with_args("rm -f  path")
    file.remove("path", force=True)

@patch("revolver.core._run")
def test_copy(run):
    run.expects_call().with_args("cp -f src dst")
    file.copy("src", "dst")

@patch("revolver.core._run")
def test_copy_force_false(run):
    run.expects_call().with_args("cp  src dst")
    file.copy("src", "dst", force=False)

@patch("revolver.core._run")
@patch("revolver.file.attributes")
def test_copy_default_attributes(run, attributes):
    run.expects_call()
    attributes.expects_call().with_args("dst", mode=None, owner=None, group=None)
    file.copy("src", "dst")

@patch("revolver.core._run")
@patch("revolver.file.attributes")
def test_copy_default_attributes(run, attributes):
    run.expects_call()
    attributes.expects_call().with_args("dst", mode="foo", owner="bar", group="baz")
    file.copy("src", "dst", mode="foo", owner="bar", group="baz")
