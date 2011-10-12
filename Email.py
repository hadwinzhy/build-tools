'''
Created on 2011-7-19

@author: zheng
'''
import email
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib
import Constant
from Utils import myprint


class Email():
    authInfo = {}
    fromAdd = ""
    toAdd = ""
    subject = ""
    plainText = ""
    
    def __init__(self, project):
        self.initData(project)
        self.sendEmail(self.authInfo, self.fromAdd, self.toAdd, self.subject, self.plainText)
        pass
    
    def initData(self, project):        
        self.authInfo['server'] = 'smtp.smedio.com.cn'
        self.authInfo['user'] = 'hadwin.zheng'
        self.authInfo['password'] = 'p@ssw1rd'
        self.fromAdd = 'hadwin.zheng@smedio.com.cn'
#        self.toAdd = ['hadwinzhy@gmail.com', 'hadwin.zheng@smedio.com.cn', 'fudaner@live.com']
        self.toAdd ='hadwin.zheng@smedio.com.cn,'
#        self.toAdd = ['mike.wu@smedio.com.cn', 'm.kohno@smedio.co.jp', 'w.kevin@smedio.co.jp', 'felix.long@smedio.com.cn', 'rejin.ren@smedio.com.cn', 'jimmy.li@smedio.com.cn', 'ivy.li@smedio.com.cn', 'hadwin.zheng@smedio.com.cn', 'cheney.li@smedio.com.cn', 'jack.chen@smedio.com.cn', 'alex.li@smedio.com.cn', 'eleven.xu@smedio.com.cn', 'bokey.zhang@smedio.com.cn','h.yamashita@smedio.co.jp','h.suzuki@smedio.co.jp']
	if(project.build_style=="nightly"):
            self.subject = project.projectName + ' ' + Constant.version + ' - Commit '+project.lastestCommit +' Nightly Build Ready'        
	elif (project.build_style=="normal"):
 	    self.subject = project.projectName + ' ' + Constant.version + ' - Commit '+project.lastestCommit +' Release Build Ready'
        self.plainText = '\
        Dear All,\n\n\
        The CableBay ' + Constant.version + ' Build is ready, and u can get it from:\n\
        China:\n\
        \t' + project.smb_addr_windows + project.remote_file_addr + '\n\
        Japan:\n\
        \t' + "ftp://"+Constant.ftp_addr +project.ftp_path+ project.remote_file_addr + '\n\n\
        Thanks,\n\n\
        Hadwin '
        
        
def sendEmail(self, authInfo, fromAdd, toAdd, subject, plainText): 
	strFrom = fromAdd
	strTo = toAdd
	server = authInfo.get('server')
	user = authInfo.get('user')
	passwd = authInfo.get('password')

	if not (server and user and passwd) :
		myprint( 'incomplete login info, exit now' )
	return

	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = subject
	msgRoot['From'] = strFrom
	msgRoot['To'] = ', '.join(self.toAdd)
	msgRoot.preamble = 'This is a multi-part message in MIME format.'

	# Encapsulate the plain and HTML versions of the message body in an
	# 'alternative' part, so message agents can decide which they want to display.
	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)

	msgText = MIMEText(plainText, 'plain', 'utf-8')
	msgAlternative.attach(msgText)

        #msgText = MIMEText(htmlText, 'html', 'utf-8')
        #msgAlternative.attach(msgText)

        #fp = open('test.jpg', 'rb')
        #msgImage = MIMEImage(fp.read())
        #fp.close()
        #msgImage.add_header('Content-ID', '<image1>')
        #msgRoot.attach(msgImage)

	smtp = smtplib.SMTP()
	smtp.set_debuglevel(1)
	smtp.connect(server)
	smtp.login(user, passwd)
	smtp.sendmail(strFrom, strTo, msgRoot.as_string())
	smtp.quit()
	return
       
