#!/usr/bin/env python
'''This reads data from a json file named "secrets.json"
Formated like this:
{
	"trello": {
		"api_key": "",
		"token":"",
	}
}
'''
import os
import json

SECRETS_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'secrets.json')
# SECRETS_FILE = '/tmp/secrets.json'

def get_secret(service, key=None):
    with open(SECRETS_FILE) as data:
        s = json.load(data)
        if key is None:
            secret = s[service]
        else:
            secret = s[service][key]
    return secret


