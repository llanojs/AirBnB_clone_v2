#!/usr/bin/python3
"""
    Fabric script for generate a .tgz archive
"""

from fabric.api import local
import datetime


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
