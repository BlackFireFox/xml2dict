#!/usr/bin/env python
import sys,os
if len(sys.argv)>1:
	try:
		if sys.argv[1]=="-u":
			if os.name=="nt":
				print os.popen("dir C:\\Python*\\Lib\\xml2dict*")
				print "Removing..."
				print "del C:\\Python*\\Lib\\xml2dict*"
				os.system("del C:\\Python*\\Lib\\xml2dict*")
				print os.popen("dir C:\\Python*\\Lib\\xml2dict*")
			else:
				if os.popen('echo $USER','r').read()=="root\n":
					f=os.popen('ls /usr/lib/python*/xml2dict*','r').read().split("\n")
					for a in f:
						if a!="":
							print "rm "+a
							os.system("rm "+a)
					if os.popen('ls /usr/lib/python*/xml2dict*','r').read()=="":
						print "Success."
					else:
						unsuc=os.popen('ls /usr/lib/python*/xml2dict*','r').read().split("\n")
						print "Unsuccess for:"
						for a in unsuc:
							if a!="":
								print a
				else:
					print "Must be root."
			sys.exit()
	except:
		pass
else:
	if os.name=="nt":
		print "Copying..."
		os.system("copy lib\\xml2dict.py C:\\Python*\\Lib")
		if "xml2dict.py" in os.popen('dir C:\\Python*\\Lib\\xml2dict*','r').read():
			print "Success."
		else:
			print "Error."
	else:
		if os.popen('echo $USER','r').read()=="root\n":
			print "Copying..."
			paths=os.popen("ls -d /usr/lib/python*/","r").read().split("\n")
			for a in paths:
				if a!="":
					print "cp lib/xml2dict.py "+a
					os.system("cp lib/xml2dict.py "+a)
			if "xml2dict.py" in os.popen('ls /usr/lib/python*/xml2dict*','r').read():
				print "Success for:"
				suc=os.popen('ls /usr/lib/python*/xml2dict*','r').read().split("\n")
				for a in suc:
					if a!="":
						print a.split("/")[3]
			else:
				print "Error."
		else:
			print "Must be root."