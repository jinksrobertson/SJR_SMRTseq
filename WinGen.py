#! /usr/bin/env python
######################################
#Author: Amy X. Guo 
#Institution: Duke University 
#Lab: Sue Jinks-Robertson Lab
######################################
import os
import glob
from itertools import tee, izip
def window (iterable,size):
	iters = tee(iterable,size)
	for i in xrange (1,size):
		for each in iters [i:]:
			next(each, None)
	return izip(*iters)

path="./"	
filename=os.listdir(path)
for file in filename:
	if file.startswith('a_'):
		OutFileName=("b_%s"%(file[2:]))
		OutFile=open(OutFileName,'w')
		handle = open(file,"rU") 
		for line in handle:
			OutFile.write(line)
			line=line.strip()
			for each in window(line,12):
				a=list(each)
				b=''.join(a)
				OutFile.write(b+'\n')
			print 'End'
		

