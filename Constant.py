'''
Created on Apr 19, 2011

@author: zheng
'''
#projects
CableBay = "Cablebay"



sdk_base_path = '/opt/android-sdk-linux_x86/'
bin_path = '/local/bin:' + sdk_base_path + 'tools:+' + sdk_base_path + 'platform-tools'
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
smb_addr_linux_path = 'smb://' + smb_addr + '/root_home/CableBay/'
smb_addr_windows_path = '\\\\' + smb_addr + '\\root_home\\CableBay\\'
ftp_addr = 'smedio.co-site.jp'
ftp_path = '/release-Build/'
version = "Beta2"


log_path = '/tmp/log.txt'
