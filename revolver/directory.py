# -*- coding: utf-8 -*-

from tempfile import mkdtemp

from cuisine import dir_attribs as attributes
from cuisine import dir_ensure as ensure
from cuisine import dir_exists as exists
from cuisine import file_attribs_get as attributes_get
from cuisine import file_is_link as is_link

from revolver.core import sudo, run

def temp_local():
    return mkdtemp()

def temp(mode=None, owner=None, group=None):
    path = run('mktemp --directory')
    attributes(path, mode=mode, owner=owner, group=group)
    return path

def remove(location, recursive=False, force=True):
    recursive = recursive and '-r' or ''
    force = force and '-f' or ''

    run('rm %s %s %s' % (force, recursive, location))

def create(path, recursive=False, mode=None, owner=None, group=None):
    recursive = recursive and '-p' or ''

    if exists(path):
        return

    run('mkdir %s %s' % (recursive, path))
    attributes(path, mode=mode, owner=owner, group=group)

