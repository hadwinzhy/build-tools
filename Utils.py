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
	print s
	fd = open ('/tmp/log.txt', 'a')
	fd.write(s +'\n')
	fd.flush()
	fd.close()


def linux2windows( url ):
	pass
