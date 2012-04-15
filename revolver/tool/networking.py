# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver import package

_TOOLS = ["curl", "nmap", "rsync", "tcpdump", "traceroute", "wget"]


def install():
    package.install(_TOOLS)


def ensure():
    package.ensure(_TOOLS)
