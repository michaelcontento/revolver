# -*- coding: utf-8 -*-

from cuisine import group_check as cuisine_get
from cuisine import group_create as cuisine_create
from cuisine import group_ensure as cuisine_ensure
from cuisine import group_user_add as cuisine_user_add
from cuisine import group_user_check as cuisine_user_check
from cuisine import group_user_ensure as cuisine_user_ensure

from revolver import group

def test_revolver_is_just_a_wrapper():
    assert group.get == cuisine_get
    assert group.create == cuisine_create
    assert group.ensure == cuisine_ensure
    assert group.user_add == cuisine_user_add
    assert group.user_check == cuisine_user_check
    assert group.user_ensure == cuisine_user_ensure
