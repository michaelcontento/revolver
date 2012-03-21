# -*- coding: utf-8 -*-

from cuisine import text_detect_eol as cuisine_detect_eol
from cuisine import text_ensure_line as cuisine_ensure_line
from cuisine import text_normalize as cuisine_spaces_normalize
from cuisine import text_nospace as cuisine_spaces_remove
from cuisine import text_replace_line as cuisine_replace_line
from cuisine import text_strip_margin as cuisine_strip_margin
from cuisine import text_template as cuisine_template
from fabric.utils import indent as fabric_indent
import cuisine

from revolver import text

def test_revolver_is_just_a_wrapper():
    assert text.detect_eol == cuisine_detect_eol
    assert text.ensure_line == cuisine_ensure_line
    assert text.indent == fabric_indent
    assert text.replace_line == cuisine_replace_line
    assert text.spaces_normalize == cuisine_spaces_normalize
    assert text.spaces_remove == cuisine_spaces_remove
    assert text.strip_margin == cuisine_strip_margin
    assert text.template == cuisine_template

    assert text.WINDOWS_EOL == cuisine.WINDOWS_EOL
    assert text.MAC_EOL == cuisine.MAC_EOL
    assert text.UNIX_EOL == cuisine.UNIX_EOL
