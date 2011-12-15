# -*- coding: utf-8 -*-

from revolver import contextmanager as ctx
from revolver.core import sudo

def command(name, command):
    sudo(
        '/etc/init.d/%(name)s %(command)s' 
        % {'name': name, 'command': command}
    )

def start(name):
    command(name, 'start')

def stop(name):
    command(name, 'stop')

def restart(name):
    command(name, 'restart')

def reload(name):
    command(name, 'reload')

def is_running(name):
    with ctx.settings(warn_only=True):
        res = sudo('/etc/init.d/%s status' % name)
        return res.succeeded
