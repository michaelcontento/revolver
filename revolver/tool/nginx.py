# -*- coding: utf-8 -*- 

from __future__ import with_statement

from revolver import command
from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import file
from revolver import package
from revolver import server
from revolver import service
from revolver.core import sudo

def install():
    already_installed = package.is_installed('nginx')

    if server.version == '10.04':
        package.install_ppa('nginx/stable')
    package.install('nginx')

    if not already_installed:
        site_disable('default')

    www_dir = '/var/www'
    www_owner = 'www-data'
    if not dir.exists(www_dir):
        with ctx.sudo():
            dir.create(www_dir)
            dir.attributes(www_dir, owner=www_owner, group=www_owner)

    restart()

def ensure():
    if command.exists('nginx'):
        return

    install()

def restart():
    service.restart('nginx')

def reload():
    service.reload('nginx')

def site_disable(site):
    with ctx.cd('/etc/nginx/sites-enabled'), ctx.sudo():
        file.remove(site)
        reload()

def site_enable(site):
    site_available = '/etc/nginx/sites-available/%s' % site
    site_enabled = '/etc/nginx/sites-enabled/%s' % site
   
    with ctx.sudo():
        file.link(site_available, site_enabled)
        reload()

def site_ensure(site, lines):
    with ctx.sudo(), ctx.cd('/etc/nginx/sites-available/'):
        file.write(site, lines)

    site_enable(site)
