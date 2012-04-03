# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver.core import sudo
from revolver import command, package


def install():
    package.ensure(["curl", "git-core", "make"])

    url = "https://raw.github.com/visionmedia/git-extras/master/bin/git-extras"
    sudo("curl -s %s | INSTALL=y sh" % url)


def ensure():
    if not command.exists("git-extras"):
        install()
