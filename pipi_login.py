#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import pexpect

try:
    paip={1:'1.1.1.1',2:'2.2.2.2'}
    papasswd={'1.1.1.1':'passwd1','2.2.2.2':'passwd2'}
    for keys,values in paip.items():
        print keys,values
    typenum=raw_input("Please input the num which is in front of the IP: ")
    Num=int(typenum)
    IpAdress=paip.get(Num)
    Passwd=papasswd.get(IpAdress)
    print ""
    print('Connect to ......')
    print(IpAdress)
    print ""
    Port=22
    hufu = pexpect.spawn('ssh root@%s -p %s'%(IpAdress,Port))
    hufu.expect('.ssword:')
    hufu.sendline(Passwd)
    hufu.interact()
except:
    print('There is sth wrong with this script! T_T')
