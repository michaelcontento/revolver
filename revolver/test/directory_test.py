# -*- coding: utf-8 -*-

from cuisine import dir_attribs as cuisine_attributes
from cuisine import dir_ensure as cuisine_ensure
from cuisine import dir_exists as cuisine_exists
from cuisine import file_attribs_get as cuisine_attributes_get
from cuisine import file_is_link as cuisine_is_link
import fudge

from revolver import directory
from revolver.directory import temp, temp_local, remove, create

def test_revolver_is_just_a_wrapper():
    assert directory.attributes == cuisine_attributes
    assert directory.attributes_get == cuisine_attributes_get
    assert directory.ensure == cuisine_ensure
    assert directory.exists == cuisine_exists
    assert directory.is_link == cuisine_is_link

@fudge.patch("revolver.directory.mkdtemp")
def test_temp_local(mkdtemp):
    mkdtemp.expects_call().returns("path")
    assert temp_local() == "path"

@fudge.patch("revolver.core._run")
@fudge.patch("revolver.directory.attributes")
def test_temp_calles_mktemp(run, attributes):
    run.expects_call().with_args("mktemp --directory").returns("foo")
    attributes.expects_call()
    assert temp() == "foo"

@fudge.patch("revolver.core._run")
@fudge.patch("revolver.directory.attributes")
def test_temp_default_attributes(run, attributes):
    run.expects_call()
    attributes.expects_call().with_args(None, mode=None, owner=None, group=None)
    temp()

@fudge.patch("revolver.core._run")
@fudge.patch("revolver.directory.attributes")
def test_temp_passes_attributes(run, attributes):
    run.expects_call().returns("path")
    attributes.expects_call().with_args("path", mode="foo", owner="bar", group="baz")
    temp("foo", "bar", "baz")

@fudge.patch("revolver.core._run")
def test_remove_defaults(run):
    run.expects_call().with_args("rm -f  path")
    remove("path")

@fudge.patch("revolver.core._run")
def test_remove_recusrive(run):
    run.expects_call().with_args("rm -f  path")
    remove("path", recursive=False)

    run.expects_call().with_args("rm -f -r path")
    remove("path", recursive=True)

@fudge.patch("revolver.core._run")
def test_remove_force(run):
    run.expects_call().with_args("rm   path")
    remove("path", force=False)

    run.expects_call().with_args("rm -f  path")
    remove("path", force=True)

@fudge.patch("revolver.core._run")
@fudge.patch("revolver.directory.exists")
def test_create_if_path_exists(run, exists):
    exists.expects_call().with_args("path").returns(True)
    create("path")

@fudge.patch("revolver.core._run")
@fudge.patch("revolver.directory.exists")
def test_create_defaults(run, exists):
    exists.expects_call().with_args("path").returns(False)
    run.expects_call().with_args("mkdir  path")
    create("path")

@fudge.patch("revolver.core._run")
@fudge.patch("revolver.directory.exists")
def test_create_recursive(run, exists):
    exists.expects_call().returns(False)
    run.expects_call().with_args("mkdir -p path")
    create("path", recursive=True)

@fudge.patch("revolver.core._run")
@fudge.patch("revolver.directory.exists")
@fudge.patch("revolver.directory.attributes")
def test_create_default_attributes(run, exists, attributes):
    run.expects_call().with_args("mkdir  path")
    exists.expects_call().returns(False)
    attributes.expects_call().with_args("path", mode=None, owner=None, group=None)
    create("path")

@fudge.patch("revolver.core._run")
@fudge.patch("revolver.directory.exists")
@fudge.patch("revolver.directory.attributes")
def test_create_default_attributes(run, exists, attributes):
    run.expects_call().with_args("mkdir  path")
    exists.expects_call().returns(False)
    attributes.expects_call().with_args("path", mode="foo", owner="bar", group="baz")
    create("path", mode="foo", owner="bar", group="baz")
