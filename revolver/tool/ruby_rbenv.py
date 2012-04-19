# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver.core import run
from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import package, file


def install():
    package.ensure("git-core")

    if not dir.exists(".rbenv"):
        run("git clone git://github.com/sstephenson/rbenv.git .rbenv")
    else:
        with ctx.cd(".rbenv"):
            run("git pull")

    _ensure_autoload(".bashrc")
    _ensure_autoload(".zshrc")


def ensure():
    if not dir.exists(".rbenv"):
        install()


def _ensure_autoload(filename):
    file.append(filename, 'export PATH="$HOME/.rbenv/bin:$PATH"')
    file.append(filename, 'eval "$(rbenv init -)"')
