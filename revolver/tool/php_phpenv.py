# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver.core import run
from revolver import directory as dir
from revolver import package


def install():
    package.ensure(["curl", "git-core"])

    url = "https://raw.github.com/CHH/phpenv/master/bin/phpenv-install.sh"
    if not dir.exists(".phpenv"):
        run("curl -s %s | bash" % url)
    else:
        run("curl -s %s | UPDATE=yes bash" % url)

    dir.create(".phpenv/versions")


def ensure():
    if not dir.exists(".phpenv"):
        install()
