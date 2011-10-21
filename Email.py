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
from Utils import myprint, linux2windows

myEmail = 'hadwin.zheng@smedio.com.cn'
authInfo = {}
authInfo['server'] = 'mail.smedio.com.cn'
authInfo['user'] = 'hadwin.zheng'
authInfo['password'] = 'p@ssw1rd'


def send( p ):
	email_list = getEmailList()
	subject = getEmailSubject( p )
	context = getEmailContext( p )
	sendEmail(email_list, context , subject)

def getEmailList():
	file = open(Constant.email_list_file)
	email_list = []
	for lines in file:
		email_list += [lines[:-1]]
	print email_list	
	#test
#	email_list = 'hadwin.zheng@smedio.com.cn'
	return email_list

def getEmailSubject( p ):
	subject = p.name + ' ' + Constant.version + ' - Commit '+p.latestCommit + ' '
	if p.build_method == Constant.build_release:
		subject += 'Release '
	elif p.build_method == Constant.build_verify:
		subject += 'Verify '
	elif p.build_method == Constant.build_nightly:
		subject += 'Nightly'
	return subject + ' Build Ready'

def getEmailContext( p ):
	contextHeader = 'Dear All,\n\n'
	contextFooter = '\n\nThanks,\nHadwin'
	contextBody = '\tThe '+p.name + ' '+ Constant.version + ' Build is ready, and u can get it from:\n\t\t'
	contextBody += linux2windows( p.smb_addr )
	context = contextHeader + contextBody + contextFooter
	print context

	return context

def sendEmail( email_list, plainText, subject):
	strFrom = myEmail
	strTo = email_list
	server = authInfo.get('server')
	user = authInfo.get('user')
	passwd = authInfo.get('password')

	if not (server and user and passwd) :
		myprint( 'incomplete login info, exit now' )
		return

	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = subject
	msgRoot['From'] = strFrom
	msgRoot['To'] = ', '.join(email_list)
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
	myprint ('sending Email...')
	smtp = smtplib.SMTP()
	smtp.set_debuglevel(1)
	smtp.connect(server)
	smtp.login(user, passwd)
	smtp.sendmail(strFrom, strTo, msgRoot.as_string())
	smtp.quit()
	myprint('Email has sent')
