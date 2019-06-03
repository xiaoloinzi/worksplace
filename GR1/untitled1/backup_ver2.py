
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/7 14:11
# @Author  : Aries
# @Site    : 
# @File    : backup_ver2.py
# @Software: PyCharm
import os
import time
source = ['F:\\ee']
target_dir = 'F:\\a'
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory',today)
target = today + os.sep + now + '.zip'
zip_command = "winRAR a '%s' %s"% (target,''.join(source))
if os.system(zip_command) == 0:
    print('successful backup to',target)
else:
    print('backup failed')