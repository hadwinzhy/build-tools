'''
Created on 2011-7-19

@author: zheng
'''


import Constant
from Utils import checkDirs
import re, os, time, subprocess

p4RemotePath = ''


def download( project ):
	init( project )
	forceDownload()
	

def init( project ):
	os.putenv("P4PORT", Constant.p4_addr)
	os.putenv("P4USER", "hadwin")
	os.putenv('P4PASSWD', '123456')
	if project.name == Constant.CableBay:
		global p4RemotePath 
		p4RemotePath = '//depot/ANDROID/BRANCH/CableBay/CableBay1.1/...'	
    #remove all project files
	print project.workspace_path
	checkDirs(project.workspace_path)


    
def forceDownload():
	print 'p4 sync -f ' + p4RemotePath + '#head' 
	p = subprocess.call('p4 sync -f ' + p4RemotePath + '#head',  stdout=open ('/tmp/log.txt' ,'w+' ), stderr=subprocess.STDOUT, shell = True)
	print stdouput
	
def getLatestCommit ( project ):
        p = subprocess.Popen('p4 changes -s submitted  -m 1 ' + p4RemotePath, shell=True \
                             , stdout=subprocess.PIPE)
        output = p.communicate(subprocess.PIPE)[0]
        pattern = re.compile(r'\D+(\d+)\D+')
        match = pattern.match(output)
        if match:   
            project.lastestCommit = match.group(1)
            today = time.strftime("%Y_%m_%d", time.localtime())
            project.folder_name = project.projectName + "_" + Constant.version + "_" + project.lastestCommit \
                + "_" + today
