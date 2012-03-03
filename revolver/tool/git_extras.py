# -*- coding: utf-8 -*- 

from __future__ import with_statement

from revolver import command
from revolver import package
from revolver.core import sudo

def install():
    package.ensure(["curl", "git-core"])

    url = "https://raw.github.com/visionmedia/git-extras/master/bin/git-extras"
    sudo("curl -s %s | INSTALL=y sh" % url)

def ensure():
    if not command.exists("git-extras"):
        install()
