# -*- coding: utf-8 -*-

from revolver.core import run
from revolver.tool import pythonbrew

def install(version, _update=True):
    pythonbrew.ensure()

    status = run("pythonbrew switch %s; true" % version)
    if status.find("not installed") != -1 or _update:
        run("pythonbrew install --no-test %s" % version)
        run("pythonbrew cleanup")
        run("pythonbrew switch %s" % version)

    run("pip install virtualenv")
    run("pip install virtualenvwrapper")

def ensure(version):
    install(version, _update=False)

