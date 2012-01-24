# -*- coding: utf-8 -*-

from fabric.api import local as fabric_local
from fabric.api import get as fabric_get
from fabric.api import env as fabric_env
from fabric.api import put as fabric_put

from revolver import core

from .utils import assert_contain_function_wrapped

def test_revolver_is_just_a_wrapper():
    assert core.env == fabric_env
    assert core.get == fabric_get
    assert core.local == fabric_local

    assert_contain_function_wrapped(core.put, fabric_put)
