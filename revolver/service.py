# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver import contextmanager as ctx
from revolver import core, file


def add_upstart(name, content):
    if name.endswith(".conf"):
        name = name[:-5]

    upstart_file = "/etc/init/%s.conf" % name

    with ctx.sudo():
        with ctx.unpatched_state():
            file.write(upstart_file, content)


def command(name, command):
    initd_file = "/etc/init.d/%s" % name
    upstart_file = "/etc/init/%s.conf" % name

    if file.exists(upstart_file):
        cmd = "%s %s" % (command, name)
    elif file.exists(initd_file):
        cmd = "%s %s" % (initd_file, command)
    else:
        cmd = "false"

    with ctx.unpatched_state():
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
