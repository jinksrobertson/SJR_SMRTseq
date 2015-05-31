#! /usr/bin/env python
######################################
#Author: Amy X. Guo 
#Institution: Duke University 
#Lab: Sue Jinks-Robertson Lab
######################################
import itertools
inputfile1 ="ForBar.txt"
inputfile2 = "RevBar.txt"
ForBar = open (inputfile1,'r')
RevBar = open( inputfile2,'r')
forward={}
reverse={}
for ForBarLine in ForBar:
	splitna=ForBarLine.split()
	key=splitna[0]
	forbalue = splitna[1]
	forbalue2 = splitna [2]
	forward[key]=[forbalue,forbalue2]
for RevBarLine in RevBar:
	splitnarev=RevBarLine.split()
	keyrev=splitnarev[0]
	forbaluerev = splitnarev[1]
	forbalue2rev = splitnarev [2]
	reverse[keyrev]=[forbaluerev,forbalue2rev]
print forward	
print reverse

for pair in itertools.product (forward,reverse): 
	result = pair
	filename= ''.join(result)
	OutFileName=("%s"%(filename))
	OutFile=open(OutFileName,'w')
	value1=forward.get(result[0])
	value2=reverse.get(result[1])
	for item in value1:
		OutFile.write("%s\n"%(item))
	for item2 in value2:
		OutFile.write("%s\n"%(item2))
	
OutFile.close()
