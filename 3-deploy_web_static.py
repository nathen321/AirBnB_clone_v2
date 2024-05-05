#!/usr/bin/python3
"""
Fabric script tha generate tar acrchive and deploy it to the web serv
folder of your AirBnB Clone repo, using the function deplooy.
"""

from datetime import datetime
from fabric.api import env, local, put, run, sudo
from os.path import exists, isdir


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
    except Exception as e:
        return None


def do_deploy(archive_path):
    """script to deploy web serv"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        sudo('mkdir -p {}{}/'.format(path, no_ext))
        sudo('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        sudo('rm /tmp/{}'.format(file_n))
        sudo('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        sudo('rm -rf {}{}/web_static'.format(path, no_ext))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as e:
        return False


def deploy():
    """ Fabric creates and distributes an archive to your web servers"""
    path = do_pack()
    if path is None:
        print("off")
        return False
    state = do_deploy(path)
    return state
