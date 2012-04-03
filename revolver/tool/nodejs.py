# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver.core import run
from revolver.tool import nodejs_nvm


def install(version, _update=True):
    nodejs_nvm.ensure()

    if not version.startswith("v"):
        version = "v" + version

    status = run("nvm use %s" % version)
    if status.find("not installed yet") != -1 or _update:
        run("nvm install %s > /dev/null" % version)

    run("nvm alias default %s" % version)


def ensure(version):
    install(version, _update=False)
