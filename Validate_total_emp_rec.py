# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:33:27 2022

@author: Danish
"""

import requests
import json
import time

from api_helper import print_request_pretty, print_response_pretty, get_endpoint


def test_post_headers_body_json():
    url = get_endpoint() + '/employees'

    # Additional headers.
    headers = {'Content-Type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}

    # Body
    payload = {}

    retry_limit = 5
    while True and retry_limit != 0:
        resp = requests.request("GET", url, headers=headers, data=payload)
        if resp.status_code != 429:
            break
        else:
            retry_limit -= 1
            time.sleep(1)

    # Validate response headers and body contents, e.g. status code.
    print('Response Code : ' + str(resp.status_code))
    assert resp.status_code == 200
    resp_body = resp.json()
    print("response body = "+str(resp_body))
    assert len(resp_body['data']) == 24

    # print full request and response
    print_request_pretty(resp.request)
    print_response_pretty(resp)