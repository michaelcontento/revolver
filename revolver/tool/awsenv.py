# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver.core import run
from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import package, file


def install():
    package.ensure(["git-core", "openjdk-7-jre"])

    if not dir.exists(".awsenv"):
        run("git clone git://github.com/michaelcontento/awsenv.git .awsenv")
        return

    with ctx.cd(".awsenv"):
        run("git pull")

    _ensure_autoload(".bashrc")
    _ensure_autoload(".zshrc")


def ensure():
    if not dir.exists(".awsenv"):
        install()


def _ensure_autoload(filename):
    file.append(filename, 'export PATH="$HOME/.awsenv/bin:$PATH"')
    file.append(filename, 'eval "$(awsenv init -)"')
