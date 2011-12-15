# -*- coding: utf-8 -*- 

from __future__ import with_statement

from revolver import command
from revolver import contextmanager as ctx
from revolver import file
from revolver import package

def install():
    package.install('stunnel')

    with ctx.sudo():
        file.sed('/etc/default/stunnel4', 'ENABLED=0', 'ENABLED=1')

def ensure():
    if not command.exists('stunnel4'):
        install()
    
