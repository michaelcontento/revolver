# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from fudge import patch

from revolver import git


@patch("revolver.core.local")
def test_revparse(local):
    cmd = "git rev-parse foo"
    local.expects_call().with_args(cmd, capture=True).returns("bar")
    assert git.revparse("foo") == "bar"


@patch("revolver.core.local")
def test_repository_name(local):
    cmd = "grep 'url' .git/config | cut -d':' -f2"
    local.expects_call().with_args(cmd, capture=True).returns("bar")
    assert git.repository_name() == "bar"


@patch("revolver.core.local")
def test_repository_name_without_trailing_git(local):
    local.expects_call().returns("bar.git")
    assert git.repository_name() == "bar"


@patch("revolver.core.local")
def test_repository_name_without_leading_directories(local):
    local.expects_call().returns("foo/faz/bar")
    assert git.repository_name() == "bar"


@patch("revolver.directory.temp_local")
@patch("revolver.core.local")
def test_archive(temp_local, local):
    temp_local.expects_call().returns("/tmp")
    cmd = "git archive --format=tar foo | gzip > /tmp/repo.tar.gz"
    local.expects_call().with_args(cmd)
    assert git.create_archive("foo")
