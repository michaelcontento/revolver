# -*- coding: utf-8 -*-

from cuisine import package_ensure as cuisine_ensure
from cuisine import package_install as cuisine_install
from cuisine import package_update as cuisine_update

from revolver import package

def test_revolver_is_just_a_wrapper():
    assert package.ensure == cuisine_ensure
    assert package.install == cuisine_install
    assert package.update == cuisine_update
