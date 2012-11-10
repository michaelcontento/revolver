# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

import fabric

from revolver import contextmanager as ctx
from revolver import decorator, core


def test_revolver_is_just_a_wrapper():
    assert decorator.hosts == fabric.decorators.hosts
    assert decorator.needs_host == fabric.network.needs_host
    assert decorator.parallel == fabric.decorators.parallel
    assert decorator.roles == fabric.decorators.roles
    assert decorator.runs_once == fabric.decorators.runs_once
    assert decorator.serial == fabric.decorators.serial
    assert decorator.task == fabric.decorators.task
    assert decorator.with_settings == fabric.decorators.with_settings


def test_multiargs():
    stack = []

    def dummy(*args, **kwargs):
        stack.append((args, kwargs))

    decorator.multiargs(dummy)([1, 2, 3])
    print stack
    assert stack == [((1,), {}), ((2,), {}), ((3,), {})]


def test_multiargs_no_argumetns():
    stack = []

    def dummy(*args, **kwargs):
        stack.append((args, kwargs))

    decorator.multiargs(dummy)()
    assert stack == [((), {})]


def test_multiargs_no_list():
    stack = []

    def dummy(*args, **kwargs):
        stack.append((args, kwargs))

    decorator.multiargs(dummy)("foo", bar="baz")
    assert stack == [(("foo",), {"bar": "baz"})]


def _sudo_dummy(sudo=None):
    return sudo


def test_sudo_dummy():
    assert _sudo_dummy() is None
    assert _sudo_dummy(True)
    assert not _sudo_dummy(False)


def test_inject_sudo_with_forced_sudo():
    with ctx.sudo():
        assert decorator.inject_use_sudo(_sudo_dummy)()


def test_inject_sudo_does_nothing_if_argument_given():
    assert decorator.inject_use_sudo(_sudo_dummy)(sudo=True)
    assert not decorator.inject_use_sudo(_sudo_dummy)(sudo=False)


def _use_sudo_dummy(use_sudo=None):
    return use_sudo


def test_sudo_dummy():
    assert _use_sudo_dummy() is None
    assert _use_sudo_dummy(True)
    assert not _use_sudo_dummy(False)


def test_inject_use_sudo_with_forced_sudo():
    with ctx.sudo():
        assert decorator.inject_use_sudo(_use_sudo_dummy)()


def test_inject_use_sudo_does_nothing_if_argument_given():
    assert decorator.inject_use_sudo(_use_sudo_dummy)(use_sudo=True)
    assert not decorator.inject_use_sudo(_use_sudo_dummy)(use_sudo=False)


def test_sudo():
    # TODO Properly mock/assert the used context
    def checker():
        assert core.env.sudo_forced
        assert core.env.sudo_user is None

    decorator.sudo(checker)()
