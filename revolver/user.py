# -*- coding: utf-8 -*-

from cuisine import user_check as get
from cuisine import user_create as create
from cuisine import user_ensure as ensure

from revolver import log

def exists(user):
    if get(user) == None:
        return False

    return True

def home_directory(user):
    user_data = get(user)
    if user_data is None: 
        log.abort('User does not exists')

    return user_data['home']
