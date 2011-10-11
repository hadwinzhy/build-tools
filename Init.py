'''
Created on 2011-7-19

@author: zheng
'''
import Constant
import os, sys
from  Project import Project
from Utils import myprint
import subprocess


def init_choice(numOfArgv):
	if ( numOfArgv < 0):
		print 'There is no argument, system exit' 
		exit()
	elif ( numOfArgv == 1 ):
		project = ask()
	
	return project	

def ask():
	choice = raw_input('Which project u want to sync:  1. '+Constant.CableBay+'\n==> Enter number to be run: \n')
	if ( choice == '1'):
		project = Project()
		project.name = Constant.CableBay		
	else :
		print 'no such project, system exit' 
		exit()
	
	#add for check latest commit	

	return project
		

def system_init():
	os.putenv('PATH', "/usr/bin:/bin:" + Constant.bin_path)   
	#init the log file
#	fd = open(Constant.log_path, 'w')
#	fd.write( '' )
#	fd.close()
	subprocess.call('tee /tmp/log.txt &',shell = True)
	myprint ('build start ...')
