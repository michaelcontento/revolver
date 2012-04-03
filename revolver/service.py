# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver import contextmanager as ctx
from revolver import core


def command(name, command):
    cmd = "/etc/init.d/%s %s" % (name, command)
    core.sudo(cmd)


def start(name):
    command(name, "start")


def stop(name):
    command(name, "stop")


def restart(name):
    command(name, "restart")


def reload(name):
    command(name, "reload")


def is_running(name):
    with ctx.settings(warn_only=True):
        res = core.sudo("/etc/init.d/%s status" % name)
        return res.succeeded
