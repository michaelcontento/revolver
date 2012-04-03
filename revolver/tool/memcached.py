# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver import command, package


def install():
    package.install(["memcached", "libmemcached-dev"])


def ensure():
    if command.exists("memcached"):
        return

    install()
