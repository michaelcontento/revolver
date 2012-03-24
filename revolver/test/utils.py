# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

import sys

def assert_contain_function_wrapped(haystack, needle):
    if sys.version.startswith("2.5."):
        # We're unable to detect the inner method so we skip the checks ...
        return

    needle_offset = str(needle).split(' ')[-1]
    haystack_offset = str(haystack.__closure__[0]).split(' ')[-1]
    assert needle_offset == haystack_offset
