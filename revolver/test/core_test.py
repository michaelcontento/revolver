# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import with_statement

from fabric.api import env as fabric_env
from fabric.api import get as fabric_get
from fabric.api import local as fabric_local
from fabric.api import put as fabric_put
from fudge import patch
import cuisine
import fabric

from revolver import core

from .utils import assert_contain_function_wrapped

def test_revolver_is_just_a_wrapper():
    assert core.env == fabric_env
    assert core.get == fabric_get
    assert core.local == fabric_local

    assert_contain_function_wrapped(core.put, fabric_put)

def test_patch_fabric_api():
    assert fabric.api.run == core.run
    assert fabric.api.sudo == core.sudo

def test_patch_fabric_operations():
    assert fabric.operations.run == core.run
    assert fabric.operations.sudo == core.sudo

def test_patch_cuisine():
    assert cuisine.run == core.run
    assert cuisine.sudo == core.sudo

def test_original_methods_are_available_but_private():
    assert core._run.__module__ == "fabric.operations"
    assert core._sudo.__module__ == "fabric.operations"
