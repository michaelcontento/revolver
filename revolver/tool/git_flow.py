# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver.core import sudo
from revolver import command, package


def install():
    package.ensure(["curl", "git-core"])

    url = "https://raw.github.com" \
        + "/nvie/gitflow/develop/contrib/gitflow-installer.sh"
    sudo("curl -s %s | bash" % url)


def ensure():
    if not command.exists("git-flow"):
        install()
