# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver import contextmanager as ctx
from revolver import file, text


def ensure(lines):
    with ctx.sudo():
        file.update('/etc/sudoers', lambda _: text.ensure_line(_, *lines))
