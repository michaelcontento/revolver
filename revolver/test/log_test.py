# -*- coding: utf-8 -*-

from fabric.contrib.console import confirm as fabric_confirm
from fabric.utils import abort as fabric_abort
from fabric.utils import fastprint as fabric_put_fast
from fabric.utils import puts as fabric_put
from fabric.utils import warn as fabric_warn

from revolver import log

def test_revolver_is_just_a_wrapper():
    assert log.confirm == fabric_confirm
    assert log.abort == fabric_abort
    assert log.put_fast == fabric_put_fast
    assert log.put == fabric_put
    assert log.warn == fabric_warn
