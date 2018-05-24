#!/usr/bin/env python3.6

import requests
req = requests.get('https://github.com/timeline.json')
a = req.json()
print (a)
