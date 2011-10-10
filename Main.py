'''
Created on 2011-7-14

@author: zheng
'''


class Project():
    projectName = ""
    sdk_path = ""
    keystore_path = ""
    lastestCommit = ""
    workspace_path = ""
    apk_file_name = ""
    folder_name = ""
    remote_file_addr = ""
    build_style=""
    ftp_addr=""
    smb_addr_windows=""
    versionCode=""
    versionName=""

    def __init__(self):
        pass    
    
    def run(self):
		pass
#        Init(self)
#        Download(self)
#        Modify(self)
#        Build(self)
#        Sign(self)
#        if os.path.exists(self.workspace_path + "bin/" + self.apk_file_name):
#	    Upload(self)
#            print "Emailing, please wait"
#            Email(self)
#            return 0;
#        else:
#            return -1 
        
class Ask():
    def __init__(self):
        pass


if __name__ == '__main__':
	Ask();
    #now the defualt is 1
    #projectNum = raw_input("what project u want to sync:\n 1.CableBay\n==> Enter number to be run\n")
#   if(len(sys.argv)<2):
#print "there is no argument,exit"
#exit()
#   projectNum = '1'
#   project = Project()
#   project.projectName = {
#       '1': Constant.CableBay,
#       '2': 2,
#    }[projectNum]   
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
