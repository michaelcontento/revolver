# -*- coding: utf-8 -*-

from fabric import colors as old

from revolver import color as new

def test_revolver_is_just_a_wrapper():
    assert new.blue == old.blue
    assert new.cyan == old.cyan
    assert new.green == old.green
    assert new.magenta == old.magenta
    assert new.red == old.red
    assert new.white == old.white
    assert new.yellow == old.yellow
