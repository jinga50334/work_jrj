#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

def getip():
    hostinput = input('Please input the url:')
    hufur=requests.get("http://119.29.29.29/d",params={'dn': requests.urllib3.get_host(hostinput)[1]},timeout=0.1)
    if hufur.headers.get('Content-Length') == str(0):
        print("The domain can not be resolved!")
    else:
        print("The real IP: %s" % (hufur.content.decode('utf-8')))

getip()