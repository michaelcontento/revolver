# -*- coding: utf-8 -*- 

from __future__ import with_statement

from revolver import command
from revolver import package
from revolver.core import sudo

def install():
    package.ensure(["curl", "git-core"])

    url = "https://raw.github.com/michaelcontento/git-chiefs/master/install"
    sudo("curl -s %s | bash" % url)

def ensure():
    if not command.exists("git-chiefs"):
        install()
