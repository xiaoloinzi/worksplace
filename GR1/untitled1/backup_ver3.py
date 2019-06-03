
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/7 14:53
# @Author  : Lin
# @Site    : 
# @File    : backup_ver3.py
# @Software: PyCharm
import os
import time
source = ['F:\\a']
target_dir = 'F:\\ee'
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
comment = raw_input('Enter a comment-->')
if len(comment) == 0:
    target = today + os.sep + now +'.zip'
else:
    target = today + os.sep + now +'_'+\
    comment.replace('','_')+'.zip'
if not os.path.exists(today):
    os.mkdir(today)
    print'successfully created directory',today
zip_command = "winRAR a '%s' %s" % (target,''.join(source))
if os.system(zip_command) == 0:
    print'successful backup to',target
else:
    print'backup failed'