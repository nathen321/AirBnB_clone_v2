#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""

from datetime import datetime
from fabric.api import run
from fabric.api import sudo
from fabric.api import *
from os.path import isdir
from os.path import isfile


env.hosts = ['100.26.239.249', '34.232.77.141']


def do_pack():
    """script that generates a .tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Expecte:
        return None


def do_deploy(archive_path):
    """script to deploy web serv"""
    try:
        if isfile(archive_path):
            file = archive_path.split("/")[-1]
            name = file.split(".")[0]
            put(archive_path, "/tmp/{}".format(file))
            sudo("rm -rf /data/web_static/releases/{}/".format(name))
            sudo("mkdir -p /data/web_static/releases/{}/".format(name))
            sudo(
                    "tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
                        file, name))
            sudo("rm -r /tmp/{}".format(file))
            sudo("rm -rf /data/web_static/current")
            s = "ln -s /data/web_static/releases/{}/ /data/web_static/current"
            sudo(s.format(name))
            return True
        else:
            return False
    except Expecte:
        return False
