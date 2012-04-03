# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

import fabric

from revolver import log


def test_revolver_is_just_a_wrapper():
    assert log.confirm == fabric.contrib.console.confirm
    assert log.abort == fabric.utils.abort
    assert log.put_fast == fabric.utils.fastprint
    assert log.put == fabric.utils.puts
    assert log.warn == fabric.utils.warn
