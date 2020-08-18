#!/usr/bin/python3
"""
    Fabric script for generate a .tgz archive
"""

from fabric.api import run, put, sudo, env, local
from os import path
import datetime

env.hosts = ['35.243.226.232', '50.19.157.176']

def do_pack():
    """
        Function to generates  a .tgz file from content
        of we_static
    """
    current = datetime.datetime.now()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz". \
        format(current.year, current.month, current.day, current.hour,
               current.minute, current.second)

    folder = local("mkdir -p versions")
    execute = local("tar -cvzf {} web_static".format(file_name))
    if execute.succeeded:
        return file_name
    else:
        None

def do_deploy(archive_path):
    """
            Function to deploy a file in distributed servers
    """
    if not path.exists(archive_path):
        return False
    try:
        print("Executing task 'do_deploy'")
        # Upload file
        put(archive_path, "/tmp/")
        # Create folder
        file_name = archive_path.split(".")[0].split("/")[1]
        folder = "/data/web_static/releases/{}/".format(file_name)
        run('mkdir -p {}'.format(folder))
        # Uncompress
        run('tar -xzf /tmp/{}.tgz -C {}'.format(file_name, folder))
        # delete file uploaded from /tmp/ folder
        run('rm /tmp/{}.tgz'.format(file_name))
        # move the information to the upper folder
        run('mv -f {}web_static/* {}'.format(folder, folder))
        # delete the simbolic link
        run('rm -rf {}/web_static'.format(folder))
        run('rm -rf /data/web_static/current')
        # Create a new the symlink /data/web_static/current on the web server,
        # linked to the new version ot the code --->
        # (/data/web_static/releases/<filename without extension>)
        run('ln -sf {} /data/web_static/current'.format(folder))
        return(True)
    except BaseException:
        return(False)

def deploy():
    """Full deployment"""
    new_file = do_pack()
    if new_file is None:
        return False
    return do_deploy(new_file)
