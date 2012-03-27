# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

import sys

import fabric

def run_result(stdout="", stderr="", return_code=0):
    result = fabric.operations._AttributeString(stdout)
    result.stderr = stderr
    result.return_code = return_code
    result.failed = return_code != 0
    result.succeeded = return_code == 0
    return result

def assert_contain_function_wrapped(haystack, needle):
    assert haystack.__module__ == needle.__module__
    assert haystack.__name__   == needle.__name__
