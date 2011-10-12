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
		myprint( 'There is no argument, system exit' ) 
		exit()
	elif ( numOfArgv == 1 ):
		project = ask()
	elif ( numOfArgv == 3):
		project = newProject(sys.argv[1])
		init_build_method(sys.argv[2], project)
	return project	


def init_build_method( choice, p):
	if ( choice == '--nightly' or choice == '1' ):
		p.build_method = Constant.build_nightly
	elif ( choice =='--release' or choice == '2' ):
		p.build_method = Constant.build_release
	elif ( choice =='--verify' or choice == '3'):
		p.build_method = Constant.build_verify
	else :
		myprint( 'no such project build method, system exit' )
		exit()



def ask():
	choice = raw_input('Which project u want to sync: \n \
	1. '+Constant.CableBay+'\n==>Please enter the number to cotinue: \n')
	#ask for which commit to build
	project = newProject( choice )
	
	choice = raw_input('Which kind of build method u want to do:\n  \
	1. nightly\n  \
	2. release\n \
	3. verify\n==>Please enter the number to cotinue: \n')
	init_build_method( choice, project )	

	return project
		
def newProject( choice ):
	if ( choice == '1' or  choice == 'cablebay') : 
		project = Project()
		project.name = Constant.CableBay
	else :
		myprint( 'no such project, system exit' )
		exit()
	return project


def system_init():
	os.putenv('PATH', "/usr/bin:/bin:" + Constant.bin_path)   
	#init the log file
	fd = open(Constant.log_path, 'w')
	fd.write( '' )
	fd.close()
