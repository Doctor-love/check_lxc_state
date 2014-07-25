#!/usr/bin/env python

# check_lxc_state -
# A simple POC Nagios/Naemon check plugin for monitoring the state
# of a container using the LXC Python 3 binding

import lxc
import sys

try:
    sys.argv[1]

except IndexError:
    print("Usage: check_lxc_state CONTAINER-NAME")
    sys.exit(3)

else:
    name = sys.argv[1]
    container = lxc.Container(name)


if not container.defined:
    print("UNKNOWN - Container %s not defined..." % name)
    sys.exit(3)


if container.state == "RUNNING":
    print("OK - Container %s is running" % name)
    sys.exit(0)

elif container.state == "STOPPED":
    print("CRITICAL- Container %s is stopped" % name)
    sys.exit(2)

else:
    print("UNKNOWN - Unexpected error!")
    sys.exit(3)
