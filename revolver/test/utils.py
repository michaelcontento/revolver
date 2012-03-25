# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

import sys

def assert_contain_function_wrapped(haystack, needle):
    assert haystack.__module__ == needle.__module__
    assert haystack.__name__   == needle.__name__
