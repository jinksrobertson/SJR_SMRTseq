#! /usr/bin/env python
######################################
#Author: Amy X. Guo 
#Institution: Duke University 
#Lab: Sue Jinks-Robertson Lab
######################################
import os
import glob

path="./"	
filename=os.listdir(path)
OutFileName="input.in"
OutFile=open(OutFileName,'w')
for file in filename:
	if file.endswith('.fna'):
		handle = open(file,"rU") 
		for line in handle:
			if line.startswith(">"):
				x=line
				x=x.strip()
				y= x[1:]
				OutFile.write(y+".fna\n"+y+"\n")
OutFile.close()
				
		