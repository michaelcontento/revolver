# -*- coding: utf-8 -*-

from cuisine import user_check as cuisine_get
from cuisine import user_create as cuisine_create
from cuisine import user_ensure as cuisine_ensure
from cuisine import user_remove as cuisine_remove

from revolver import user

def test_revolver_is_just_a_wrapper():
    assert user.get == cuisine_get
    assert user.create == cuisine_create
    assert user.ensure == cuisine_ensure
    assert user.remove == cuisine_remove
