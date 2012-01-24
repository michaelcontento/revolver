# -*- coding: utf-8 -*-

from cuisine import user_check as cuisine_get
from cuisine import user_create as cuisine_create
from cuisine import user_ensure as cuisine_ensure

from revolver import user

def test_revolver_just_wrapps_cuisine():
    assert user.get == cuisine_get
    assert user.create == cuisine_create
    assert user.ensure == cuisine_ensure
