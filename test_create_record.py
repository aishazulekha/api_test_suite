import requests
import json
import time

from api_helper import print_request_pretty, print_response_pretty, get_endpoint


def test_create_record():
    url = get_endpoint() + '/create'

    # Additional headers.
    headers = {'Content-Type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}

    # Body
    payload = json.dumps({"name": "Aisha", "salary": "123", "age": "23"})

    retry_limit = 5
    while True and retry_limit != 0:
        resp = requests.request("POST", url, headers=headers, data=payload)
        if resp.status_code != 429:
            break
        else:
            retry_limit -= 1
            time.sleep(1)

    # Validate response headers and body contents, e.g. status code.
    print('Response Code : ' + str(resp.status_code))
    assert resp.status_code == 200
    resp_body = resp.json()
    print("Response Text : " + str(resp_body))
    print("Response Message : " + resp_body['message'])
    assert resp_body['message'] == 'Successfully! Record has been added.'

    # print full request and response
    print_request_pretty(resp.request)
    print_response_pretty(resp)