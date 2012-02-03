'''
Created on 2011-7-19

@author: zheng
'''


import Constant
from Utils import checkDirs
import re, os, time, subprocess

p4RemotePath = ''


def download( p ):
	init( p )
	forceDownload()
	p.latestCommit = getLatestCommit()	

def init( p ):
	os.putenv("P4PORT", Constant.p4_addr)
	os.putenv("P4USER", "hadwin")
	os.putenv('P4PASSWD', '123456')
	if p.name == Constant.CableBay:
		global p4RemotePath 
		p4RemotePath = '//depot/ANDROID/BRANCH/CableBay/CableBay1.1/...'	
    #remove all p files
	checkDirs(p.workspace_path)


    
def forceDownload():
	command = 'p4 sync -f ' + p4RemotePath + '#head' 
	subprocess.call(command + ' | ' + Constant.log_command, shell = True)

	
def getLatestCommit ():
	pipe = subprocess.Popen('p4 changes -s submitted  -m 1 ' + p4RemotePath, shell=True , stdout=subprocess.PIPE)
	output = pipe.communicate(subprocess.PIPE)[0]
	pattern = re.compile(r'\D+(\d+)\D+')
	result = pattern.match(output)
	if result:   
		latestCommit = result.group(1)
	return latestCommit


def getDescribe ( p , preCommit ):
	#test
	commits = []
	preCommit = '15578'
	command = 'p4 changes -s submitted ' + p4RemotePath 
	pipe = subprocess.Popen(command + ' | ' + Constant.log_command, shell=True , stdout=subprocess.PIPE)
	output = pipe.communicate(subprocess.PIPE)[0]
	lines = re.split('\n', output)
	for line in lines:
		pattern = re.compile ('Change (\d+) on')
		result = pattern.match(line)
		if result :
			num = result.group(1)
			if num <= p.latestCommit and num >= preCommit :
				print num
				commits += [num]
	for num in commits:
		command = 'p4 describe -s ' + num
		pipe = subprocess.Popen(command + ' | ' + Constant.log_command, shell=True , stdout=subprocess.PIPE)
		output = pipe.communicate(subprocess.PIPE)[0]
		print output



