'''
Created on 2011-7-14

@author: zheng
'''

import Constant, Init, P4, Build, Sign, Upload, Email

import sys



if __name__ == '__main__':
	
	Init.system_init()

	project=Init.init_choice(len(sys.argv))

	project.project_init()

	P4.download( project )
	
	Build.build( project )

	Sign.sign( project)		

	Upload.upload( project )

	Email.send( project )

#    project.apk_file_name = project.projectName + ".apk"
#    if(sys.argv[1]=='--normal'):
#	project.build_style="normal"
#    elif (sys.argv[1]=='--nightly'):
#	project.build_style="nightly"
#    else:
#        print "no such argv, exit"
#        exit()
#    result = project.run()    
#    
#    if result < 0:
#        print "Failed"
#    else: 
#        print "Success"
