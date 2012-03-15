# -*- coding: utf-8 -*-

from cuisine import user_check as get
from cuisine import user_create as create
from cuisine import user_ensure as ensure
from cuisine import user_remove as remove

from revolver import log

def _get_with_abort(username):
    username_data = get(username)
    if username_data is None:
        log.abort("username does not exists")
    return username_data

def exists(username):
    if get(username) == None:
        return False

    return True

def home_directory(username):
    return _get_with_abort(username)["home"]

def shell(username):
    return _get_with_abort(username)["shell"]
