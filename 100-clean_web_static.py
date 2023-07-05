#!/usr/bin/python3
"""Delete out-of-date archives."""
from fabric.api import run, local, env
import os

env.hosts = ['100.25.166.233', '52.86.149.92']


def do_clean(number=0):
    """Delete out-of-date archives."""
    number = int(number)
    if number < 1:
        number = 1

    local_archives = sorted(os.listdir("versions"))
    number_to_keep = number if number >= 2 else 1

    for archive in local_archives[:-number_to_keep]:
        local("rm versions/{}".format(archive))

    with cd('/data/web_static/releases'):
        run("ls -ltr")
        run_archives = run("ls -ltr | awk 'NF{print $NF}'").split()
        run_archives = sorted(run_archives)
        number_to_keep = number if number >= 1 else 0

        for archive in run_archives[:-number_to_keep]:
            run("rm -rf releases/{}".format(archive))
