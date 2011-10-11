'''
Created on Apr 20, 2011

@author: zheng
'''
import os, sys
from shutil import rmtree

import Constant
    
def checkDirs(dir_path):
    if(os.path.exists(dir_path)):
        rmtree(dir_path)
        os.mkdir(dir_path)
    else:
        os.mkdir(dir_path)


def myprint ( s ):
	fd = open ('/tmp/log.txt', 'w+')
	fd.write(s);
	fd.close
