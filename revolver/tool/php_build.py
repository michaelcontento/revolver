# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import package, file, core


def install():
    package.ensure(["curl", "git-core"])

    if not dir.exists(".php-build"):
        core.run("git clone git://github.com/CHH/php-build .php-build")

    with ctx.cd(".php-build"):
        core.run("git pull")
        dir.create("versions")
        dir.create("tmp")

    _ensure_autoload(".bashrc")
    _ensure_autoload(".zshrc")


def ensure():
    if not dir.exists(".php-build"):
        install()


def _ensure_autoload(filename):
    file.append(filename, 'export PATH="$HOME/.php-build/bin:$PATH"')
