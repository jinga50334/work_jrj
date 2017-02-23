#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# writen by yjw
import requests

try:
    r=requests.get('http://hufu.com:80',timeout=0.3)
    status=r.ok
    if status==True:
        print(1)
    else:
        print(0)
except:
    print('There is sth wrong!')
