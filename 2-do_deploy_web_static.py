#!/usr/bin/python3
"""
    Fabric script for deploy the file in distributed
    servers
"""

from fabric.api import run, put, sudo, env
from os import path
import datetime

env.hosts = ['35.243.226.232', '50.19.157.176']


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
		file_name = archive_path.split(".")[0]
		folder = "/data/web_static/releases/{}/".format(file_name)
		run("mkdir -p {}".format(folder))
		# Uncompress
		run("tar -xzf /tmp/{} -C {}".format(archive_path, folder))
	        # delete file uploaded from /tmp/ folder
		run("rm /tmp/{}".format(archive_path))
	        # move the information to the upper folder
		run("mv {}/web_static/* {}".format(folder, folder))
		# delete the simbolic link
		run("rm -rf {}/web_static".format(folder))
		run("rm -rf /data/web_static/current")
		# Create a new the symlink /data/web_static/current on the web server,
	        # linked to the new version ot the code --->
        	# (/data/web_static/releases/<filename without extension>)
		run("ln -s {} /data/web_static/current".format(folder))
		return(True)
	except BaseException:
	        return(False)
