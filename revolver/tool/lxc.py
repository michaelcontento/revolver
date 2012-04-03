# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, with_statement

from revolver import contextmanager as ctx
from revolver import file, package, core

_LXC_NETWORK = """\
lxc.network.type=veth
lxc.network.link=vbr-%(name)s
lxc.network.flags=up
"""

_NETWORK_TEMPLATE = """\
<network>
  <name>%(name)s</name>
  <bridge name="vbr-%(name)s" />
  <forward/>
  <ip address="192.168.%(subnet)d.1" netmask="255.255.255.0">
    <dhcp>
      <range start="192.168.%(subnet)d.2" end="192.168.%(subnet)d.254" />
    </dhcp>
  </ip>
</network>
"""

_DEFAULT_NAME = "lxc"
_DEFAULT_SUBNET = 42


def install(name=_DEFAULT_NAME, subnet=_DEFAULT_SUBNET, _update=True):
    packages = ["lxc", "debootstrap", "libvirt-bin"]
    if _update:
        package.install(packages)
    else:
        package.ensure(packages)

    networks = _list_networks()
    if name not in networks:
        _create_network(name, subnet)
        core.run("virsh net-start %s" % name)
    else:
        if not networks[name]:
            core.run("virsh net-start %s" % name)

    with ctx.sudo():
        config = _LXC_NETWORK % dict(name=name, subnet=subnet)
        file.write("/etc/lxc/net-lxc.conf", config, mode="a+r")


def ensure(name=_DEFAULT_NAME, subnet=_DEFAULT_SUBNET):
    install(name=name, subnet=subnet, _update=False)


def _create_network(name, subnet):
    tempfile = file.temp()
    try:
        definition = _NETWORK_TEMPLATE % dict(name=name, subnet=subnet)
        file.write(tempfile, definition)
        core.run("virsh net-define %s" % tempfile)
        core.run("virsh net-autostart %s" % name)
    finally:
        file.remove(tempfile)


def _list_networks():
    """Return a dictionary of network name to active status bools.

        Sample virsh net-list output::

    Name                 State      Autostart
    -----------------------------------------
    default              active     yes
    juju-test            inactive   no
    foobar               inactive   no

    Parsing the above would return::
    {"default": True, "juju-test": False, "foobar": False}

    See: http://goo.gl/kXwfC
    """
    output = core.run("virsh net-list --all")
    networks = {}

    # Take the header off and normalize whitespace.
    net_lines = [n.strip() for n in output.splitlines()[2:]]
    for line in net_lines:
        if not line:
            continue
        name, state, auto = line.split()
        networks[name] = state == "active"
    return networks
