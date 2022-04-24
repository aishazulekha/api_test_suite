import requests
import json
import time

from api_helper import print_request_pretty, print_response_pretty, get_endpoint


def test_update_record():
    url = get_endpoint() + '/update/15'

    # Additional headers.
    headers = {'Content-Type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}

    # Body
    payload = json.dumps({"employee_name": "Zulekha", "employee_salary": "654", "employee_age": "27"})

    retry_limit = 5
    while True and retry_limit != 0:
        resp = requests.request("PUT", url, headers=headers, data=payload)
        if resp.status_code != 429:
            break
        else:
            retry_limit -= 1
            time.sleep(1)

    # Validate response headers and body contents, e.g. status code.
    print('Response Code : ' + str(resp.status_code))
    assert resp.status_code == 200
    resp_body = resp.json()
    resp_msg = resp_body['message']
    resp_changed_name = resp_body['data']['employee_name']
    resp_changed_salary = resp_body['data']['employee_salary']
    resp_changed_age = resp_body['data']['employee_age']
    assert resp_msg == 'Successfully! Record has been updated.' and resp_changed_name == 'Zulekha' and resp_changed_salary == "654" and resp_changed_age == "27"

    # print full request and response
    print_request_pretty(resp.request)
    print_response_pretty(resp)