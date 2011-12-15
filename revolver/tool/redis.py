# -*- coding: utf-8 -*- 

from __future__ import with_statement

from revolver import command
from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import package
from revolver.core import sudo, run

_VERSION = '2.4'
_OPTIONS = ''

def install(version=_VERSION, options=_OPTIONS):
    package.ensure(['git-core', 'build-essential'])
    tmpdir = dir.temp()

    try:
        with ctx.cd(tmpdir):
            run('git clone git://github.com/antirez/redis.git ./ --depth 1')
            run('git checkout %s' % version)
            run('make %s > /dev/null' % options)
            sudo('make install')
    finally:
        dir.remove(tmpdir, recursive=True)

def ensure(version=_VERSION, options=_OPTIONS):
    # TODO Check if version if fulfilled
    if command.exists('redis-server'):
        return

    install(version, options)
