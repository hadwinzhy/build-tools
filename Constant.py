'''
Created on Apr 19, 2011

@author: zheng
'''
#projects
CableBay = "CableBay"


sdk_base_path = '/opt/android-sdk-linux_x86/'
bin_path = '/local/bin:' + sdk_base_path + 'tools:' + sdk_base_path + 'platform-tools'
google_map_libs = sdk_base_path + '/add-ons/addon_google_apis_google_inc_11/libs/maps.jar'


workspace_base_path = '/local/p4workspace/hadwin-workspace/ANDROID/'
tmp_path = '/tmp/apk/'
tools_path = '/local/tools/SignatureToolKDDI/'
keystore_base_path = '/local/tools/key/'
password = "android"
alias = "androiddebugkey"

#p4 
p4_addr = '192.168.10.14:1960'

#samba and ftp
smb_addr = '192.168.10.44'
smb_addr_base_path = 'smb://' + smb_addr + '/QAServer/'
#ftp_addr = 'smedio.co-site.jp'
#ftp_path = '/release-Build/'
version = "GM5"


log_path = '/tmp/log.txt'
log_command = 'tee -a ' + log_path


#build method
build_verify = 'verify'
build_release = 'release'
build_nightly = 'nightly'

email_list_file = 'email.txt'
