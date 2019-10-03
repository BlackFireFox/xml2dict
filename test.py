#!/usr/bin/env python
import os,xml2dict
di=""
while not os.path.isfile(di):
	di=raw_input("File xml: ")
xml=xml2dict.x2d(di)
print xml
print "----"
print xml2dict.d2x(xml)