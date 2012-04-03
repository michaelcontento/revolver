# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver import command, file, package
from revolver import contextmanager as ctx


def install():
    package.install('stunnel')

    with ctx.sudo():
        file.sed('/etc/default/stunnel4', 'ENABLED=0', 'ENABLED=1')


def ensure():
    if not command.exists('stunnel4'):
        install()
