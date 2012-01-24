# -*- coding: utf-8 -*- 

from __future__ import with_statement

from revolver import command
from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import package
from revolver.core import sudo, run

_VERSION = 'v0.6'
_OPTIONS = ''

def install(version=_VERSION, options=_OPTIONS):
    package.ensure(['git-core', 'libssl-dev', 'curl', 'build-essential'])
    tmpdir = dir.temp()

    try:
        with ctx.cd(tmpdir):
            repo = 'git://github.com/joyent/node.git' 
            run('git clone %s ./ --depth 1' % repo)
            run('git checkout %s' % version)
            run('./configure %s' % options)
            run('make > /dev/null')
            sudo('make install')
    finally:
        dir.remove(tmpdir, recursive=True)

def ensure(version=_VERSION, options=_OPTIONS):
    # TODO Check if version if fulfilled
    if command.exists('node'):
        return

    install(version, options)
