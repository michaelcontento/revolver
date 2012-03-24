# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import with_statement

from cuisine import command_check as cuisine_exists

from revolver import command

def test_revolver_is_just_a_wrapper():
    assert command.exists == cuisine_exists
