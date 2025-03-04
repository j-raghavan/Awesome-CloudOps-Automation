##
##  Copyright (c) 2021 unSkript, Inc
##  All rights reserved.
##
import pprint
from typing import List,Any
from pydantic import BaseModel, Field
from google.cloud.compute_v1.services.instances import InstancesClient


class InputSchema(BaseModel):
    project: str = Field(
        title = "GCP Project",
        description = "GCP Project Name"
    )
    zone: str = Field(
        title = "Zone",
        description = "GCP Zone where instance list should be gotten from"
    )


def gcp_get_instances_without_label_printer(output):
    if len(output) == 0:
        return
    pprint.pprint(output)


def gcp_get_instances_without_label(handle, project: str, zone:str) -> List:
    """gcp_get_instances_without_label Returns the List of compute instances

        :type project: string
        :param project: Google Cloud Platform Project

        :type zone: string
        :param zone: Zone to which the instance list in the project should be fetched.

        :rtype: List of instances
    """
    output = []
    ic = InstancesClient(credentials=handle)
    try:
        result = ic.list(project=project, zone=zone)
        instance_list = []
        for instance in result:
            instance_list.append(instance.name)
        for instance_name in instance_list:
            result = ic.get(project=project, zone=zone, instance=instance_name)
            if not result.labels:
                output.append(instance_name)
    except Exception as error:
        output.append(error)

    return output
