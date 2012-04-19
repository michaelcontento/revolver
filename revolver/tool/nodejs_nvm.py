# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver.core import run
from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import package


def install():
    package.ensure(["git-core", "libssl-dev", "curl", "build-essential"])

    if not dir.exists(".nvm"):
        run("git clone git://github.com/creationix/nvm.git .nvm")
    else:
        with ctx.cd(".nvm"):
            run("git pull")

    _ensure_autoload(".bashrc")
    _ensure_autoload(".zshrc")


def ensure():
    if not dir.exists(".nvm"):
        install()


def _ensure_autoload(filename):
    file.append(filename, 'source "$HOME/.nvm/nvm.sh"')
