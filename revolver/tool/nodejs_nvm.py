# -*- coding: utf-8 -*-

from __future__ import with_statement

from revolver.core import run
from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import package

def install():
    package.ensure(["git-core", "libssl-dev", "curl", "build-essential"])

    if not dir.exists(".nvm"):
        run("git clone git://github.com/creationix/nvm.git .nvm")
        return

    with ctx.cd(".nvm"):
        run("git pull")

def ensure():
    if not dir.exists(".nvm"):
        install()
