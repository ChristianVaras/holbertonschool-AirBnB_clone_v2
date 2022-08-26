#!/usr/bin/python3
"""script that deploy archive!"""

from os.path import exists
from fabric.api import env, put, run
env.hosts = ['54.173.35.192', '54.221.151.240']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:

        # web_static_20170315003959.tgz
        only_file = archive_path.split("/")[-1]

        # web_static_20170315003959
        only_name = only_file.split(".")[0]

        # /data/web_static/releases/web_static_20170315003959/
        path = "/data/web_static/releases/" + only_name + "/"
        put(archive_path, "/tmp/")
        run("mkdir -p {:s}".format(path))
        run("tar -xzf /tmp/{:s} -C {:s}".format(only_file, path))
        run("rm /tmp/{:s}".format(only_file))
        run("mv {:s}web_static/* {:s}".format(path, path))
        run("rm -rf {:s}web_static".format(path))
        link = "/data/web_static/current"
        run("rm -rf {:s}".format(link))
        run("ln -s {:s} {:s}".format(path, link))
        print("New version deployed!")
        return True

    except Exception:
        return False
