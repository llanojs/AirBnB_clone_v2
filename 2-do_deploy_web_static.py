#!/usr/bin/python3
"""
    Fabric script for deploy the file in distributed
    servers
"""

from fabric.api import run, put, sudo
from os import path
import datetime

env.hosts = ['<IP web-01>', 'IP web-02']


def do_deploy(archive_path):
    """
        Function to deploy a file in distributed servers
    """
    if not path.exists(archive_path):
        return False
    try:
        print("Executing task 'do_deploy'")
        # Upload file
        put(archive_path, / tmp/)
        # Create folder
	file_name = archive_path.split(".")[0]
	file_name = "/data/web_static/releases/{}".format(directory)
	run("mkdir -p {}".format(file_name)
        # Uncompress
	run("tar -xzf /tmp/{} -C {}".format(archive_path, file_name)
        # delete file uploaded from /tmp/ folder
        #
        return(True)
    except BaseException:
        return(False)
