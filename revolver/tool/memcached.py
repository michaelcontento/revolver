# -*- coding: utf-8 -*-

from revolver import command
from revolver import package

def install():
    package.install(["memcached", "libmemcached-dev"])

def ensure():
    if command.exists("memcached"):
        return

    install()

