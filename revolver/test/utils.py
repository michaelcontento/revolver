# -*- coding: utf-8 -*-

def assert_contain_function_wrapped(haystack, needle):
    needle_offset = str(needle).split(' ')[-1]
    haystack_offset = str(haystack.__closure__[0]).split(' ')[-1]
    assert needle_offset == haystack_offset
