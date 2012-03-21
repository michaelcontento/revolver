# -*- coding: utf-8 -*-

from fabric import decorators as old_decorator
from fabric.network import needs_host as fabric_needs_host

from revolver.decorator import inject_use_sudo
from revolver.decorator import multiargs
from revolver import contextmanager as ctx
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

def test_multiargs():
    args = []
    def dummy(arg):
        args.append(arg)

    multiargs(dummy)([1, 2, 3])
    assert args == [1, 2, 3]

def _sudo_dummy(use_sudo=None):
    return use_sudo

def test_sudo_dummy():
    assert _sudo_dummy() == None
    assert _sudo_dummy(True)
    assert not _sudo_dummy(False)

def test_inject_sudo_with_forced_sudo():
    with ctx.sudo():
        assert inject_use_sudo(_sudo_dummy)()

def test_inject_sudo_does_nothing_if_argument_given():
    assert inject_use_sudo(_sudo_dummy)(use_sudo=True)
    assert not inject_use_sudo(_sudo_dummy)(use_sudo=False)

def _use_sudo_dummy(use_sudo=None):
    return use_sudo

def test_sudo_dummy():
    assert _use_sudo_dummy() == None
    assert _use_sudo_dummy(True)
    assert not _use_sudo_dummy(False)

def test_inject_use_sudo_with_forced_sudo():
    with ctx.sudo():
        assert inject_use_sudo(_use_sudo_dummy)()

def test_inject_use_sudo_does_nothing_if_argument_given():
    assert inject_use_sudo(_use_sudo_dummy)(use_sudo=True)
    assert not inject_use_sudo(_use_sudo_dummy)(use_sudo=False)
