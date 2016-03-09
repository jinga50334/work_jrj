#!/usr/bin/python
# -*- coding: UTF-8 -*-
import commands
_usemem0=float(commands.getoutput("/usr/local/bin/redis-cli -h 127.0.0.1 -p 6379 info |grep 'used_memory'  |egrep 'used_memory:'|awk -F: {'print $2'}"))
_maxmem0=float(commands.getoutput("/usr/local/bin/redis-cli -h 127.0.0.1 -p 6379 config get maxmemory|egrep -v maxmemory"))

if _usemem0 >= _maxmem0*0.95:
    print(10)
elif _usemem0 >= _maxmem0*0.9:
    print(5)
else:
    print(1)