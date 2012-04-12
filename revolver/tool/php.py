# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver.core import run
from revolver import contextmanager as ctx
from revolver import directory as dir
from revolver import file, package
from revolver.tool import php_build, php_phpenv


def install(version, fpm=False, xdebug=False):
    php_build.ensure()
    php_phpenv.ensure()

    switched = run("phpenv global %s; true" % version)
    if not switched == "":
        _install_php(version, fpm, xdebug)
        run("phpenv global %s" % version)

    run("phpenv rehash")
    _install_apc()
    _install_composer()


def _install_php(version, fpm, xdebug):
    package.ensure([
        "build-essential", "lemon", "libbz2-dev", "libpcre3-dev",
        "libc-client2007e-dev", "libcurl4-gnutls-dev", "libexpat1-dev",
        "libfreetype6-dev", "libgmp3-dev", "libicu-dev", "libjpeg8-dev",
        "libltdl-dev", "libmcrypt-dev", "libmhash-dev", "libpng12-dev",
        "libreadline-dev", "libssl1.0.0", "libssl-dev", "libt1-dev",
        "libtidy-dev", "libxml2-dev", "libxslt1-dev", "re2c", "zlib1g-dev"
    ])

    def configure(value):
        key = "PHP_BUILD_CONFIGURE_OPTS"
        return 'export %(key)s="%(value)s $%(key)s"' % locals()

    prefix = "$HOME/.phpenv/versions/%s" % version

    # Force the usage of pear because pyrus is unable to install APC
    # See https://github.com/CHH/php-build/blob/master/man/php-build.1.ronn#L79
    pear_path = "%s/pear" % prefix
    pear = configure("--with-pear=%s" % pear_path)
    dir.ensure(pear_path, recursive=True)

    # We only support this two configuration options! Why?
    # - Xdebug is already integrated into php-build
    # - FPM is a very common flag
    #
    # But if you want to configure php even further? Own definition files!
    # See https://github.com/CHH/php-build/blob/master/man/php-build.1.ronn#L54
    fpm = (fpm and configure("--enable-fpm")) or "true"
    xdebug = (xdebug and "true") or 'export PHP_BUILD_XDEBUG_ENABLE="off"'

    with ctx.prefix(pear):
        with ctx.prefix(xdebug):
            with ctx.prefix(fpm):
                run("php-build %s %s" % (version, prefix))

    # Some executables (like php-fpm) aren't available through phpenv without
    # this symlinks
    with ctx.cd(prefix):
        run('find sbin/ -type f -exec ln -sf "$(pwd)/{}" -t "$(pwd)/bin" \;')


def _install_apc():
    installed = run("pecl list | grep -i apc; true")
    if installed:
        return

    run("yes '' | pecl install apc")

    bin_path = run("phpenv which php")
    conf_path = bin_path.replace("/bin/php", "/etc/conf.d")
    file.write(conf_path + "/apc.ini", "extension=apc.so")


def _install_composer():
    # TODO Implement this
    pass
