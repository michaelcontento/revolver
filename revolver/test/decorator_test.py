# -*- coding: utf-8 -*-

from fabric import decorators as old_decorator
from fabric.network import needs_host as fabric_needs_host

from revolver import decorator

def test_revolver_is_just_a_wrapper():
    assert decorator.hosts == old_decorator.hosts
    assert decorator.needs_host == fabric_needs_host
    assert decorator.parallel == old_decorator.parallel
    assert decorator.roles == old_decorator.roles
    assert decorator.runs_once == old_decorator.runs_once
    assert decorator.serial == old_decorator.serial
    assert decorator.task == old_decorator.task
    assert decorator.with_settings == old_decorator.with_settings
