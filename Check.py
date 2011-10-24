import os,re

manifest_file_path = ''
ctx = ''
def check( p ):
	getManifestFile( p )	
	flag = checkManifestDebugFlag( )
	if flag == 'false':
		switchManifestDebugFalse()
	if p.build_method == Constant.build_release :
		addVersion ()

def getManifestFile ( p ):
	global manifest_file_path
	manifest_file_path = p.workspace_path + "AndroidManifest.xml"
	if not os.path.exists( manifest_file_path ):
		print "AndroidManifest.xml not found"
		exit()

def checkManifestDebugFlag ():
	flag = ''
	global ctx 
	manifest_file = open (manifest_file_path, 'r')
	for line in manifest_file:
		pattern = re.compile(".*debuggable=\"\s*(\w+)\s*\"")
		result = pattern.match(line)
		if result:
			flag = result.group(1)
			if flag == 'false':
				print "AndroidManifest debug is false, OK!"
				ctx += line
			elif flag == 'true':
				print "AndroidManifest debug is true, need switch to false" 
				tmp = re.compile ('true')
				ctx += tmp.sub('false', line)
			else:
				print "not such flag " + flag
		else :
			ctx += line
	manifest_file.close()
	return flag
	

def switchManifestDebugFalse ():
	write_file =open (manifest_file_path, 'w')
	write_file.write(ctx)
	write_file.close()
	

def addVersion ():
	pass
