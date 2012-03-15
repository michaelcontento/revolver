# -*- coding: utf-8 -*-

from __future__ import with_statement

from cuisine import system_uuid as uuid

from revolver import contextmanager as ctx
from revolver import file
from revolver.core import run

def timezone(zone='UTC'):
    with ctx.sudo():
        from_file = '/usr/share/zoneinfo/%s' % zone
        to_file = '/etc/localtime'

        file.copy(from_file, to_file)

def version():
    return run('lsb_release --release --short')

def codename():
    return run('lsb_release --codename --short')
