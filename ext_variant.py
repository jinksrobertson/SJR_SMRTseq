#! /usr/bin/env python
######################################
#Author: Amy X. Guo 
#Institution: Duke University 
#Lab: Sue Jinks-Robertson Lab
######################################
import os
import glob
import fnmatch

OutFileName = "variants.txt"
OutFile=open(OutFileName,'w')
path="./"	
filename=os.listdir(path)
for file in filename:
	if fnmatch.fnmatch (file, '*variants'):
# 		print file
		handle = open(file,"rU")  
		for line in handle:
			if not line.startswith("#"):
# 				print line
				line=line.strip()
				OutFile.write(line+'\n')
