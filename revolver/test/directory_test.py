# -*- coding: utf-8 -*-

from cuisine import dir_attribs as cuisine_attributes
from cuisine import dir_ensure as cuisine_ensure
from cuisine import dir_exists as cuisine_exists
from cuisine import file_attribs_get as cuisine_attributes_get
from cuisine import file_is_link as cuisine_is_link

from revolver import directory

def test_revolver_is_just_a_wrapper():
    assert directory.attributes == cuisine_attributes
    assert directory.attributes_get == cuisine_attributes_get
    assert directory.ensure == cuisine_ensure
    assert directory.exists == cuisine_exists
    assert directory.is_link == cuisine_is_link
