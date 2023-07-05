#!/usr/bin/python3
"""Create and distribute an archive to web servers."""
from fabric.api import local, put, run, env
import os
from datetime import datetime

env.hosts = ['100.25.166.233','52.86.149.92']


def do_pack():
    """Generate tgz file."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)
    local("tar -cvzf {} web_static".format(archive_path))
    return archive_path


def do_deploy(archive_path):
    """Distribute an archive to the web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        archive_name_no_ext = os.path.splitext(archive_name)[0]

        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_name_no_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.
            format(archive_name, archive_name_no_ext))
        run('rm /tmp/{}'.format(archive_name))
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.
            format(archive_name_no_ext, archive_name_no_ext))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_name_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.
            format(archive_name_no_ext))
        return True
    except:
        return False


def deploy():
    """Create and distribute an archive to the web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)

deploy()
