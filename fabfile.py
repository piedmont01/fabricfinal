import os
import re
import boto3
from fabric.api import *
from fabric.tasks import Task
from fabric.contrib import files


def generate_ip_list(profile):
    running_instances = []
    full_list = []
    filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]

    session = boto3.Session(profile_name=profile)
    ec2_resource = session.resource('ec2')
    instances = ec2_resource.instances.filter(Filters=filters)
    for instance in instances:
        running_instances.append(instance.private_ip_address.strip('\n'))
        try:
            for tags in instance.tags:
                if tags["Key"] == 'Name'
                    append.full_list[
                        {
                            tags["Value"],
                            instance.private_ip_address.strip('\n')
                        }
                    ]
                    break
        except:
            print('No tag')
