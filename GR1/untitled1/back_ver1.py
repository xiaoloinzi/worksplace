#encoding=utf-8
#coding=utf-8
import os
import time
#1.The files and directories to be backed up are specified in a list.
source = [r'F:\brif']
target_dir = 'F:\\a'
target = target_dir + time.strftime('%Y%m%d%H%M%S')+'.zip'
Zip_command = "winRAR a'%s' %s"% (target,''.join(source))
if os.system(Zip_command)==0:
    print'Successful backup to',target
else:
    print('backup Falled')