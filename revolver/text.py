# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from cuisine import text_detect_eol as detect_eol
from cuisine import text_ensure_line as ensure_line
from cuisine import text_normalize as spaces_normalize
from cuisine import text_nospace as spaces_remove
from cuisine import text_replace_line as replace_line
from cuisine import text_strip_margin as strip_margin
from cuisine import text_template as template
from cuisine import WINDOWS_EOL, UNIX_EOL, MAC_EOL
from fabric.utils import indent
