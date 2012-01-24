# -*- coding: utf-8 -*-

from cuisine import file_attribs as cuisine_attributes
from cuisine import file_attribs_get as cuisine_attributes_get
from cuisine import file_local_read as cuisine_read_local
from cuisine import file_read as cuisine_read
from cuisine import file_update as cuisine_update
from cuisine import file_write as cuisine_write

from revolver import file

def test_revolver_is_just_a_wrapper():
    assert file.attributes == cuisine_attributes
    assert file.attributes_get == cuisine_attributes_get
    assert file.read == cuisine_read
    assert file.read_local == cuisine_read_local
    assert file.update == cuisine_update
    assert file.write == cuisine_write
