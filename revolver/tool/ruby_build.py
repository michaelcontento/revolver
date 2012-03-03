# -*- coding: utf-8 -*-

from __future__ import with_statement

from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import package
from revolver.core import run
from revolver.tool import ruby_rbenv

def install():
    package.ensure("git-core") 
    ruby_rbenv.ensure()

    dir.ensure(".rbenv/plugins")
    with ctx.cd(".rbenv/plugins"):
        if not dir.exists("ruby-build"):
            run("git clone git://github.com/sstephenson/ruby-build.git")
            return

        with ctx.cd("ruby-build"):
            run("git pull")

def ensure():
    if not dir.exists(".rbenv/plugins/ruby-build"):
        install()
