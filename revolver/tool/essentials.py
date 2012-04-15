# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver import package

_TOOLS = [
    "exuberant-ctags", "vim-nox",
    "ack-grep", "apt-show-versions", "tree", "aespipe"
]


def install():
    package.install(_TOOLS)


def ensure():
    package.ensure(_TOOLS)
