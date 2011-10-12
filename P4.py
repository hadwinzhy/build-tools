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
	print 'p4 sync -f ' + p4RemotePath + '#head' 
	subprocess.call('p4 sync -f ' + p4RemotePath + '#head  |' + Constant.log_command, shell = True)

	
def getLatestCommit ():
		p = subprocess.Popen('p4 changes -s submitted  -m 1 ' + p4RemotePath, shell=True , stdout=subprocess.PIPE)
		output = p.communicate(subprocess.PIPE)[0]
		pattern = re.compile(r'\D+(\d+)\D+')
		match = pattern.match(output)
		if match:   
			lastestCommit = match.group(1)
		return lastestCommit
#            today = time.strftime("%Y_%m_%d", time.localtime())
#            p.folder_name = p.pName + "_" + Constant.version + "_" + p.lastestCommit \
#               + "_" + today
