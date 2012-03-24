# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver.core import sudo
from revolver import command, package

def install():
    package.ensure(["curl", "git-core"])

    url = "https://raw.github.com/michaelcontento/git-chiefs/master/install"
    sudo("curl -s %s | bash" % url)

def ensure():
    if not command.exists("git-chiefs"):
        install()
