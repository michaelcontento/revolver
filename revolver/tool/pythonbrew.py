# -*- coding: utf-8 -*- 

from revolver import command
from revolver import package
from revolver.core import run

def install():
    package.ensure("curl")

    if not command.exists("pythonbrew"):
        url = "https://raw.github.com/utahta/pythonbrew/master/pythonbrew-install" 
        run("curl -s %s | bash" % url)
    else: 
        run("pythonbrew update")

def ensure():
    if not command.exists("pythonbrew"):
        install()
