#!/usr/bin/env python
######################################
#Author: Amy X. Guo 
#Institution: Duke University 
#Lab: Sue Jinks-Robertson Lab
######################################
import os
import glob
path="./"	
filename=os.listdir(path)
for file in filename:
	if file.startswith('a_'):
		infileName="ref.txt"
		infile=open(infileName,'r')
		OutFileName=("%s.fna"%(file[2:]))
		OutFile=open(OutFileName,'w')
		handle = open(file,"rU") 
		arr=[]
		for line in handle:
			line=line.strip()
			arr.append(line)
		ref=[]
		for text in infile:
			text=text.strip()
			ref.append(text)
		forward = arr[0]
		middle=ref[0]
		reverse=arr[3]
		final=forward + middle +reverse 
		OutFile.write('>%s\n' %(file[2:]))
		OutFile.write(final)
		handle.close()
		OutFile.close()
			
		

