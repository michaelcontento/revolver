# -*- coding: utf-8 -*- 

from revolver import command
from revolver import package
from revolver import server
from revolver import service
from revolver.core import sudo

def install(fpm=False):
    server_version = server.version()
    apache_was_installed = package.is_installed('apache2.2-bin')

    packages = [
        'php5-suhosin', 'php5-mysql', 'php5-memcache', 'php5-memcached', 
        'php5-mcrypt', 'php5-json', 'php5-cli', 'php-apc', 'php5-dev', 
        'php5-curl', 'php-pear', 'php5-gd'
    ]
    if fpm:
        packages.append('php5-fpm')

    # Add the ppa for old ubuntu versions
    if fpm and server_version == '10.04':
        package.install_ppa('brianmercer/php')

    package.install(packages)

    # Some old php packages requires apache2 which we cannot remove
    # but we can stop it and remove it from to boot process
    if server_version != '11.10' and not apache_was_installed:
        sudo('update-rc.d -f apache2 remove')
        service.stop('apache2')

    if fpm:
        sudo('sudo update-rc.d -f php5-fpm defaults')
        service.restart('php5-fpm')

def ensure(fpm=False):
    if command.exists('php5'):
        return

    install(fpm=fpm)
    
def _generate_pear_or_pecl_name(package, channel=None, version=None, state=None):
    if channel:
        package = "%s/%s" % (channel, package)

    if version and state:
        raise ValueError("You cannot specify version AND state.")

    if version or state:
        package = "%s-%s" % (package, version or state)
    
    return package

def ensure_pear(package, channel=None, version=None, state=None):
    package = _generate_pear_or_pecl_name(package, channel, version, state)
    # TODO Check if already installed
    sudo("pear install %s; true" % package)

def ensure_pecl(package, channel=None, version=None, state=None):
    package = _generate_pear_or_pecl_name(package, channel, version, state)
    # TODO Check if already installed
    sudo("pecl install %s; true" % package)

