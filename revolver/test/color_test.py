# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

import fabric

from revolver import color


def test_revolver_is_just_a_wrapper():
    assert color.blue == fabric.colors.blue
    assert color.cyan == fabric.colors.cyan
    assert color.green == fabric.colors.green
    assert color.magenta == fabric.colors.magenta
    assert color.red == fabric.colors.red
    assert color.white == fabric.colors.white
    assert color.yellow == fabric.colors.yellow
