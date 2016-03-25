#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#writen by yjw
import commands

itougu_judge=str('works')
_itougu_out=str(commands.getoutput("curl -s -H 'Host:sso.jrj.com.cn' 'http://172.16.171.137/sso/echo.jsp'|grep works"))
def itougu_check(_itougu_out):
        if _itougu_out==itougu_judge:
                print '0'
        else:
                print '1'
itougu_check(_itougu_out)
