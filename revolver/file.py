# -*- coding: utf-8 -*-

from cuisine import file_attribs as attributes
from cuisine import file_attribs_get as attributes_get
from cuisine import file_local_read as read_local
from cuisine import file_read as read
from cuisine import file_update as update
from cuisine import file_write as write
from fabric.contrib.files import append
from fabric.contrib.files import comment
from fabric.contrib.files import contains
from fabric.contrib.files import exists
from fabric.contrib.files import sed
from fabric.contrib.files import uncomment

from revolver.core import sudo, run
from revolver.decorator import inject_use_sudo

append = inject_use_sudo(append)
comment = inject_use_sudo(comment)
contains = inject_use_sudo(contains)
exists = inject_use_sudo(exists)
sed = inject_use_sudo(sed)
uncomment = inject_use_sudo(uncomment)

def remove(location, recursive=False, force=True):
    force = force and '-f' or ''
    recursive = recursive and '-r' or ''

    run('rm %s %s %s' % (force, recursive, location))

def touch(location):
    run('touch %s' % location)

def copy(source, destination, force=True, mode=None, owner=None, group=None):
    force = force and '-f' or ''

    run('cp %s %s %s' % (force, source, destination))
    attributes(destination, mode, owner, group)

def link(source, destination, symbolic=True, force=True, mode=None, owner=None, group=None):
    force = force and '-f' or ''
    symbolic = symbolic and '-s' or ''

    run('ln %s %s "%s" "%s"' % (symbolic, force, source, destination))
    attributes(destination, mode, owner, group)
