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
					if tmp.isdigit():
						exec("%s[n]=int(tmp)"%w)
					elif tmp.startswith("-") and tmp[1:].isdigit():
						exec("%s[n]=int(tmp)"%w)
					elif "." in tmp and tmp.split(".")[-1].isdigit():
						if tmp.split(".")[0].isdigit() and tmp.split(".")[-1].isdigit():
							exec("%s[n]=float(tmp)"%w)
						elif tmp.split(".")[0].startswith("-") and tmp.split(".")[0][1:].isdigit() and tmp.split(".")[-1].isdigit():
							exec("%s[n]=float(tmp)"%w)
						else:
							exec("%s[n]=tmp"%w)
					else:
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
				xml+=str(dic[e])
			elif type(dic[e])==type({}):
				innerdict(dic[e])
				xml+="\n"+"\t"*(t-1)
			else:
				xml+=str(dic[e])
			t-=1
			xml+="</"+e+">"
	global t;t=0
	for e in di:
		xml+="\n"+"\t"*t+"<"+e+">"
		t+=1
		if type(di[e])==type([]):
			xml+=str(di[e])
		elif type(di[e])==type({}):
			innerdict(di[e])
			xml+="\n"+"\t"*(t-1)
		else:
			xml+=str(di[e])
		t-=1
		xml+="</"+e+">"
	return xml