# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

import cuisine

from revolver import group

def test_revolver_is_just_a_wrapper():
    assert group.get == cuisine.group_check
    assert group.create == cuisine.group_create
    assert group.ensure == cuisine.group_ensure
    assert group.user_add == cuisine.group_user_add
    assert group.user_check == cuisine.group_user_check
    assert group.user_ensure == cuisine.group_user_ensure
