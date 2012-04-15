# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import package
from revolver.core import run
from revolver.tool import ruby_rbenv


def install():
    package.ensure("git-core")
    package.ensure([
        "build-essential", "zlib1g-dev", "libssl-dev",
        "libxml2-dev", "libsqlite3-dev"
    ])
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
