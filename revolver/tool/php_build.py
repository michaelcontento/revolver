# -*- coding: utf-8 -*-

from __future__ import with_statement

from revolver.core import run
from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import package

def install():
    package.ensure(["curl", "git-core"])

    if not dir.exists(".php-build"):
        run("git clone git://github.com/CHH/php-build .php-build")

    with ctx.cd(".php-build"):
        run("git pull")
        dir.create("versions")
        dir.create("tmp")

def ensure():
    if not dir.exists(".php-build"):
        install()
