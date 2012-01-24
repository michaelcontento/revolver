# -*- coding: utf-8 -*-

from cuisine import text_ensure_line as cuisine_ensure_line
from fabric.utils import indent as fabric_indent

from revolver import text

def test_revolver_is_just_a_wrapper():
    assert text.ensure_line == cuisine_ensure_line
    assert text.indent == fabric_indent
