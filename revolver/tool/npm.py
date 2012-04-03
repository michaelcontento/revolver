# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver.core import sudo
from revolver import command
from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver.tool import nodejs


def install():
    nodejs.ensure()
    tmpdir = dir.temp()

    try:
        with ctx.cd(tmpdir):
            sudo('curl http://npmjs.org/install.sh | sh')
    finally:
        dir.remove(tmpdir, recursive=True)


def ensure():
    if command.exists('npm'):
        return

    install()
