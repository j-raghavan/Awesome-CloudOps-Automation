##
##  Copyright (c) 2021 unSkript, Inc
##  All rights reserved.
##
from typing import List
from pydantic import BaseModel
import pprint

class InputSchema(BaseModel):
    pass

def datadog_list_all_monitors_printer(output):
    if output is None:
        return
    pprint.pprint(output)


def datadog_list_all_monitors(handle) -> List:
    """datadog_get_all_monitors gets all monitors

        :rtype: The list of monitors.
    """
    monitor_response = handle.Monitor.get_all()
    if len(monitor_response) == 0:
        raise Exception("No monitors found")

    return monitor_response
