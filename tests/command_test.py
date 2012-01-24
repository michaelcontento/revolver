# -*- coding: utf-8 -*-

from cuisine import command_check as cuisine_exists

from revolver import command

def test_revolver_just_wrapps_cuisine():
    assert command.exists == cuisine_exists
