# -*- coding: utf-8 -*- 

from __future__ import with_statement

from revolver import command
from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import package
from revolver.core import sudo, run

def install():
    package.ensure(['git-core', 'curl', 'build-essential'])
    tmpdir = dir.temp()

    try:
        with ctx.cd(tmpdir):
            repo = 'git://github.com/sstephenson/ruby-build.git'
            run('git clone %s ./ --depth 1' % repo)
            sudo('./install.sh')
    finally:
        dir.remove(tmpdir, recursive=True)

def ensure():
    if command.exists('ruby-build'):
        return

    install()
