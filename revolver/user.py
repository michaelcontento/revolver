# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from cuisine import user_check as get
from cuisine import user_create as create
from cuisine import user_ensure as ensure
from cuisine import user_remove as remove

from revolver import log

def _get_with_abort(username):
    username_data = get(username)
    if username_data is None:
        log.abort("User '%s' does not exists" % username)
    return username_data

def exists(username):
    if get(username) == None:
        return False

    return True

def home_directory(username):
    data = _get_with_abort(username)
    if not data:
        return None
    else:
        return data["home"]

def shell(username):
    data = _get_with_abort(username)
    if not data:
        return None
    else:
        return data["shell"]
