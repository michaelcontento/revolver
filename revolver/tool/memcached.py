# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import with_statement

from revolver import command
from revolver import package

def install():
    package.install(["memcached", "libmemcached-dev"])

def ensure():
    if command.exists("memcached"):
        return

    install()

