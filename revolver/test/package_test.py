# -*- coding: utf-8 -*-

from cuisine import package_ensure as cuisine_ensure
from cuisine import package_install as cuisine_install
from cuisine import package_update as cuisine_update
from cuisine import package_upgrade as cuisine_upgrade

from revolver import package

from .utils import assert_contain_function_wrapped

def test_revolver_is_just_a_wrapper():
    assert package.upgrade == cuisine_upgrade

    assert_contain_function_wrapped(package.ensure, cuisine_ensure)
    assert_contain_function_wrapped(package.install, cuisine_install)
    assert_contain_function_wrapped(package.update, cuisine_update)
