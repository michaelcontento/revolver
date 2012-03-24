# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

import cuisine
import fabric

from revolver import text

def test_revolver_is_just_a_wrapper():
    assert text.detect_eol == cuisine.text_detect_eol
    assert text.ensure_line == cuisine.text_ensure_line
    assert text.indent == fabric.utils.indent
    assert text.replace_line == cuisine.text_replace_line
    assert text.spaces_normalize == cuisine.text_normalize
    assert text.spaces_remove == cuisine.text_nospace
    assert text.strip_margin == cuisine.text_strip_margin
    assert text.template == cuisine.text_template

    assert text.WINDOWS_EOL == cuisine.WINDOWS_EOL
    assert text.MAC_EOL == cuisine.MAC_EOL
    assert text.UNIX_EOL == cuisine.UNIX_EOL
