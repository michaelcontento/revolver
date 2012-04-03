# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from cuisine import system_uuid as uuid

from revolver import contextmanager as ctx
from revolver import file, core


def timezone(zone='UTC'):
    from_file = '/usr/share/zoneinfo/%s' % zone
    to_file = '/etc/localtime'

    with ctx.sudo():
        file.copy(from_file, to_file)


def version():
    return core.run('lsb_release --release --short').stdout


def codename():
    return core.run('lsb_release --codename --short').stdout
