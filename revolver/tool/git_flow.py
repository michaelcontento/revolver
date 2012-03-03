# -*- coding: utf-8 -*- 

from __future__ import with_statement

from revolver import command
from revolver import package
from revolver.core import sudo

def install():
    package.ensure(["curl", "git-core"])

    url = "https://raw.github.com/nvie/gitflow/develop/contrib/gitflow-installer.sh"
    sudo("curl -s %s | bash" % url)

def ensure():
    if not command.exists("git-flow"):
        install()
