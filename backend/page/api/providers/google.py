import json
import random
import string

import requests
from urllib3.connectionpool import xrange

from backend.settings import GOOGLE_PROJECT

url_template = "https://www.googleapis.com/deploymentmanager/v2/projects/" + GOOGLE_PROJECT + "/global/deployments"
url_template_list = "https://www.googleapis.com/deploymentmanager/v2beta1/projects/" + GOOGLE_PROJECT + "/global/deployments"


def _deploy(data: dict, token: str):
    payload = str(data)
    headers = {
        'Authorization': "Bearer " + token,
        'Content-Type': "application/json",
    }
    # response = requests.request("POST", url_deploy, data=payload, headers=headers)
    # return response.text
    return {"state": 0}


def _get_list(token: str):
    headers = {
        'Authorization': "Bearer " + token,
        'Content-Type': "application/json",
    }
    response = requests.request("GET", url_template, headers=headers)
    return json.loads(response.text)


def _create_content(data: dict, token: str):
    payload = {
        "name": ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(26)]).lower(),
        "target": {
            "config": {
                "content": data
            }
        }
    }
    payload = str(payload)
    headers = {
        'Authorization': "Bearer " + token,
        'Content-Type': "application/json",
    }
    response = requests.request("POST", url_template, data=payload, headers=headers)
    return json.loads(response.text)