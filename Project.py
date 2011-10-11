import Constant

class Project():
	name = "" #CableBay
	workspace4_path = ""

	def project_init(self):
		if self.name == Constant.CableBay:
			self.sdk_path = Constant.sdk_base_path + "android-11/"
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

