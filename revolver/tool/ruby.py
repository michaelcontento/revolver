# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver.core import run
from revolver.tool import ruby_build, ruby_rbenv


def install(version, _update=True):
    ruby_rbenv.ensure()
    ruby_build.ensure()

    status = run("rbenv global %s; true" % version)
    if not status == "" or _update:
        run("rbenv install %s" % version)
        run("rbenv global %s" % version)

    run("rbenv rehash")
    run("gem install --no-ri --no-rdoc bundler")


def ensure(version):
    install(version, _update=False)
