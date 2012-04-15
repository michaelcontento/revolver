# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver.core import run
from revolver import directory as dir
from revolver import package, file


def install():
    package.ensure(["curl", "git-core"])

    url = "https://raw.github.com/CHH/phpenv/master/bin/phpenv-install.sh"
    if not dir.exists(".phpenv"):
        run("curl -s %s | bash" % url)
    else:
        run("curl -s %s | UPDATE=yes bash" % url)

    dir.create(".phpenv/versions")

    _ensure_autoload(".bashrc")
    _ensure_autoload(".zshrc")


def ensure():
    if not dir.exists(".phpenv"):
        install()


def _ensure_autoload(filename):
    # TODO: Make sure that `~/.rbenv/bin` takes precedence in the PATH over
    #       `~/.phpenv/bin` by placing it before, so rbenv gets used from
    #       `~/.rbenv`. For more informations: https://github.com/CHH/phpenv
    file.append(filename, 'export PATH="$HOME/.phpenv/bin:$PATH"')
    file.append(filename, 'eval "$(phpenv init -)"')
