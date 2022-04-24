
import requests
import json
import time

from api_helper import print_request_pretty, print_response_pretty, get_endpoint


def test_employee_details():
    url = get_endpoint() + '/employee/15'

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
    print("name = "+resp_body['data']['employee_name'])
    assert resp_body['data']['employee_name'] == "Tatyana Fitzpatrick"

    # print full request and response
    print_request_pretty(resp.request)
    print_response_pretty(resp)