# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:55:07 2022

@author: Danish
"""

def print_request_pretty(request):
    print( '\n{}\n{}\n\n{}\n\n{}\n'.format(
        '-----------Request----------->',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        request.body)
    )

def print_response_pretty(response):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        response.text)
    )

def get_endpoint():
    return 'https://dummy.restapiexample.com/api/v1'