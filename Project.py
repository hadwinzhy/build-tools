import Constant

class Project():
	name = '' #CableBay
	workspace_path = ''
	latestCommit = ''
	prevCommit = ''
	sdk_version = '' #11
	build_method = '' #verify release nightly
	smb_addr = ''
	
	def project_init(self):
		if self.name == Constant.CableBay:
			self.sdk_version = '11'
			self.sdk_path = Constant.sdk_base_path + 'platforms/android-' + self.sdk_version + '/'
			self.keystore_path = Constant.keystore_base_path + "sMedio-sh-android-keystore"
			self.workspace_path = Constant.workspace_base_path + "BRANCH/CableBay/CableBay1.1/"

#        Init(self)
#        Download(self)
#        Modify(self)
#        Build(self)
#        Sign(self)
#        if os.path.exists(self.workspace_path + "bin/" + self.apk_file_name):
#       Upload(self)
#            print "Emailing, please wait"
#            Email(self)
#            return 0;
#        else:
#            return -1 

