#!/usr/bin/env python
def x2d(file):
	xmlf=open(file,"r")
	xml=xmlf.read()
	xmlf.close()
	di={}
	xml=xml.replace("    ","").replace("	","").replace("\n","").replace("\t","")
	xmlr=xml.split("<")
	da=["di"]
	for e in xmlr:
		if not e.startswith("?") and e!="":
			if not e.startswith("/"):
				n=e[:[pos for pos,char in enumerate(e) if char==">"][-1]]
				if len(e)>[pos for pos,char in enumerate(e) if char==">"][-1]+1:
					tmp=e[[pos for pos,char in enumerate(e) if char==">"][-1]+1:len(e)]
					w=da[0]
					for d in da:
						if d!=da[0]:
							w=w+"['"+d+"']"
					exec("%s[n]=tmp"%w)
				else:
					w=da[0]
					for d in da:
						if d!=da[0]:
							w=w+"['"+d+"']"
					tmp={}
					exec("%s[n]=tmp"%w)
					da.append(n)
			else:
				if e[1:[pos for pos,char in enumerate(e) if char==">"][-1]] in da:
					da.remove(e[1:[pos for pos,char in enumerate(e) if char==">"][-1]])
	return di
def d2x(di):
	global xml;xml='<?xml version="1.0" encoding="utf-8"?>'
	def innerdict(dic):
		global xml;global t
		for e in dic:
			xml+="\n"+"\t"*t+"<"+e+">"
			t+=1
			if type(dic[e])==type([]):
				xml+="\n"+"\t"*t+str(dic[e])
			elif type(dic[e])==type({}):
				innerdict(dic[e])
			else:
				xml+="\n"+"\t"*t+str(dic[e])
			t-=1
			xml+="\n"+"\t"*t+"<"+e+">"
	global t;t=0
	for e in di:
		xml+="\n"+"\t"*t+"<"+e+">"
		t+=1
		if type(di[e])==type([]):
			xml+="\n"+"\t"*t+str(di[e])
		elif type(di[e])==type({}):
			innerdict(di[e])
		else:
			xml+="\n"+"\t"*t+str(di[e])
		t-=1
		xml+="\n"+"\t"*t+"<"+e+">"
	return xml