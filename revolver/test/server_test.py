# -*- coding: utf-8 -*-

from cuisine import system_uuid as cuisine_uuid

from revolver import server

def test_revolver_is_just_a_wrapper():
    assert server.uuid == cuisine_uuid
