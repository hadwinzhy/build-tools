'''
Created on 2011-7-19

@author: zheng
'''
import subprocess
import Constant
from Utils import myprint


def sign( p ):
	command = "jarsigner -verbose -keystore " + p.keystore_path + " -signedjar "\
			+ p.workspace_path + "bin/" + p.name +".apk "\
			+ p.workspace_path + "bin/" + p.name + "_unsigned.apk " + " " + Constant.alias
                    
        #os.chdir(Constant.tmp_path)
        #command = "jarsigner -verbose -keystore " + p.keystore_path + "-sigfile CERT " \
        #            + "SHI11.apk" + " LISMO"
	p = subprocess.Popen(command + '|' + Constant.log_command, shell=True, stdin=subprocess.PIPE)
	p.communicate(Constant.password)[0]
        #os.rename("SHI11.apk", "SHI11_signed.apk")
	myprint( "singed complete" )
