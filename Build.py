'''
Created on 2011-7-19

@author: zheng
'''

from Utils import checkDirs, myprint
import subprocess
import glob
import os
import Constant

def build(  p ):
	checkFile( p )
	buildAIDL( p )
	buildR( p )
	buildJava( p )
	buildDex( p )
	buildRes( p )
	buildApk( p )
    
def checkFile(p):
	checkDirs( p.workspace_path + "gen")
	checkDirs( p.workspace_path + "bin")
	checkDirs( p.workspace_path + "assets")

   
        
def buildR(p):
	command = "aapt package -f -v -M " +  p.workspace_path + "AndroidManifest.xml -I " \
                    +  p.sdk_path + "android.jar -S " +  p.workspace_path + "res/ -m -J " \
                    +  p.workspace_path + "gen -A " +  p.workspace_path + "assets -F "  \
                    +  p.workspace_path + "bin/resources.ap --target-sdk-version " + p.sdk_version
	subprocess.call(command + '|'+ Constant.log_command, shell=True)
        
def buildAIDL(p):
	pattern = '*.aidl'
	for root, dirs, files in os.walk( p.workspace_path + "src"):
		result = glob.glob(os.path.join(root, pattern))
		for f in result:
			path = f;
			f = f.replace("aidl", "java")
			f = f.replace("src", "gen")
			command = "aidl -p" +  p.sdk_path + "framework.aidl -I" +  p.workspace_path + "src/ -I" \
                            +  p.workspace_path + "gen/ " + path + " " + f 
			subprocess.call(command + '|'+ Constant.log_command, shell=True)

def buildJava(p):
	java_list = ' '
	libs = ""
	pattern = '*.java'
	for root, dirs, files in os.walk( p.workspace_path):
		result = glob.glob(os.path.join(root, pattern))
		for f in result:
			java_list += f + " "

	pattern = '*.jar'
	for root, dirs, files in os.walk( p.workspace_path + "libs"):
		result = glob.glob(os.path.join(root, pattern))
		for f in result:
			libs += f + ":"
        
	if  p.name == Constant.CableBay:
		libs += Constant.google_map_libs
           
	command = "javac -bootclasspath " +  p.sdk_path + "android.jar -classpath " + libs + " -d "\
                 +  p.workspace_path + "bin  -Xlint:unchecked" + java_list
	myprint( command ) 
	subprocess.call(command + '|'+ Constant.log_command, shell=True)
        
def buildDex(p):
	command = "dx --verbose --dex --output=" +  p.workspace_path + "bin/classes.dex " \
                +  p.workspace_path + "bin/ " +  p.workspace_path + "libs"
	subprocess.call(command + '|'+ Constant.log_command, shell=True)
        
def buildRes(p):
	command = "aapt package -f -v -M " +  p.workspace_path + "AndroidManifest.xml -S " \
                +  p.workspace_path + "res -A " +  p.workspace_path + "assets/ -I " \
                +  p.sdk_path + "android.jar -F " +  p.workspace_path + "bin/resources.ap"
	subprocess.call(command + '|'+ Constant.log_command, shell=True)
        
def buildApk(p):
	command = "apkbuilder " +  p.workspace_path + "bin/" +  p.name \
               + "_unsigned.apk -v -u -z " +  p.workspace_path + "bin/resources.ap -f " \
               +  p.workspace_path + "bin/classes.dex -nf " +  p.workspace_path + "libs/"
	subprocess.call(command + '|'+ Constant.log_command, shell=True)
