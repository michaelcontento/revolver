# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

import cuisine

from revolver import command


def test_revolver_is_just_a_wrapper():
    assert command.exists == cuisine.command_check
