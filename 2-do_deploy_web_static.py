#!/usr/bin/python3
# deploying webservers with Fabric
from fabric.api import *
from fabric.operations import put, run, sudo
import time
import os.path

env.hosts = ['34.74.135.225', '35.196.217.180']
# env.use_ssh_config = True


def do_deploy(archive_path):
    """ function to deploy """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        put(archive_path, "/tmp")
        archive_full = (archive_path.split("/")[-1])
        archive_file = archive_full.split(".")
        run("sudo mkdir -p /data/web_static/releases/{}".format
            (archive_file[0]))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format
            (archive_full, archive_file[0]))
        run("sudo rm /tmp/{}".format(archive_full))
        run("sudo mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}".format(archive_file[0], archive_file[0]))
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(archive_file[0]))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{} \
        /data/web_static/current".format(archive_file[0]))
        return True
    except:
        return False
