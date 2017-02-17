#!/data/servers/python2.7.8/bin/python
# -*- coding: UTF-8 -*-
# writen by yjw
import redis 
import socket

try:
   localIP = socket.gethostbyname(socket.gethostname())
   r=redis.Redis(host=localIP,port=7000)
   ReSult=r.ping()
   if ReSult==True:
      print(1)
   #print(localIP,ReSult)
except:
   print(0)
