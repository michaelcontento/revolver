# -*- coding: utf-8 -*- 

from __future__ import with_statement

import re

from revolver import command
from revolver.core import sudo, run
from revolver.tool import ruby_build

_VERSION = '1.9.2-p290'

def _convert_version_to_string(version):
    return ''.join(re.findall(r'\d+', version))

def install(version=_VERSION):
    target = '/usr/local/ruby-%s' % version
    priority = _convert_version_to_string(version) 
    placeholder = {'target': target, 'priority': priority}
    
    ruby_build.ensure()
    sudo('ruby-build %s %s' % (version, target))

    update_alternatives_cmd = """sudo update-alternatives \
--install /usr/bin/ruby   ruby   %(target)s/bin/ruby %(priority)s \
--slave   /usr/bin/erb    erb    %(target)s/bin/erb \
--slave   /usr/bin/gem    gem    %(target)s/bin/gem \
--slave   /usr/bin/irb    irb    %(target)s/bin/irb \
--slave   /usr/bin/rake   rake   %(target)s/bin/rake \
--slave   /usr/bin/rdoc   rdoc   %(target)s/bin/rdoc \
--slave   /usr/bin/ri     ri     %(target)s/bin/ri \
--slave   /usr/bin/testrb testrb %(target)s/bin/testrb \
--slave   /usr/share/man/man1/erb.1  erb.1  %(target)s/share/man/man1/erb.1 \
--slave   /usr/share/man/man1/irb.1  irb.1  %(target)s/share/man/man1/irb.1 \
--slave   /usr/share/man/man1/rake.1 rake.1 %(target)s/share/man/man1/rake.1 \
--slave   /usr/share/man/man1/ri.1   ri.1   %(target)s/share/man/man1/ri.1 \
--slave   /usr/share/man/man1/ruby.1 ruby.1 %(target)s/share/man/man1/ruby.1 
"""
    sudo(update_alternatives_cmd % placeholder)
    sudo('update-alternatives --set ruby %(target)s/bin/ruby' % placeholder)

def ensure(version=_VERSION):
    if command.exists('ruby'):
        raw_installed_version = run('ruby -v | cut -d" " -f2')
        installed_version = _convert_version_to_string(raw_installed_version)
    else:
        installed_version = '0'
    
    required_version = _convert_version_to_string(version)
    if installed_version < required_version:
        install(version)
