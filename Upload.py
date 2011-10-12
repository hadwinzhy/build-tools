'''
Created on 2011-7-19

@author: zheng
'''

import smbc
import os
import Constant
from ftplib import FTP
from Utils import myprint 

#    def __init__( p):
#        self.local_file_name = p.workspace_path + "bin/" + p.apk_file_name
#        self.uploadSamba(p)
#        self.uploadFTP(p)

def upload( p ):
	pre_path = Constant.smb_addr_base_path + p.name + '/'
	
	if ( p.build_method == Constant.build_nightly or p.build_method == Constant.build_verify):
		uploadSamba( p, pre_path + "Nightly_Build/" + p.latestCommit + '/')
	elif ( p.build_method == Constant.build_release ):
		#upload both release folder and nightly folder
		uploadSamba( p, pre_path + "Nightly_Build/" + p.latestCommit + '/' )
		uploadSamba( p, pre_path + "Release_Build/" + p.latestCommit + '/' )


def uploadSamba ( p , folder_path):
	#smb://192.168.10.44/root_home/CableBay/Nightly_build/15555/CableBay.apk'
	ctx = smbc.Context ()
	p.smb_addr = folder_path + p.name + '.apk'
	ctx.mkdir( folder_path, 755 )
	remote_file = ctx.open (p.smb_addr, os.O_CREAT | os.O_WRONLY)
	local_file = open(p.workspace_path + "bin/" + p.name + '.apk')
	remote_file.write(local_file.read())
	myprint ( 'upload '+ p.smb_addr + '...' )

'''        
    def uploadFTP( p):
        print 'upload ftp'
        ftp = FTP(Constant.ftp_addr)
        ftp.login('cablebay', 'smi0801bew')
        print "login success"
	if(p.build_style=="nightly"):
	    p.ftp_path=Constant.ftp_path + "Nightly_Build/"	
	elif(p.build_style=="normal"):
	    p.ftp_path=Constant.ftp_path
        ftp.mkd(p.ftp_path + p.folder_name)
        ftp.cwd(p.ftp_path + p.folder_name)
        print self.local_file_name
        f = open(self.local_file_name, 'rb')               
        ftp.storbinary('STOR ' + p.apk_file_name, f)
        ftp.retrlines('LIST')
'''
