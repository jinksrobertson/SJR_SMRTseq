#! /usr/bin/env python
######################################
#Author: Amy X. Guo 
#Institution: Duke University 
#Lab: Sue Jinks-Robertson Lab
######################################
import sys
import os
import glob
from Bio import SeqIO
from Bio.Alphabet import generic_dna
import array
path="./"	
filename=os.listdir(path)
for file in filename:
	if file.startswith('b_'):
		OutFileName=("%s"%(file[2:]))
		OutFile=open(OutFileName,'w')
		handle = open(file,"rU") 
		arr=[]
		for line in handle:
			line=line.strip()
			arr.append(line)
		fseq= arr[0:12]
		rseq=arr[12:25]
		print fseq
		print rseq
		handle.close()
		InputFileName="ccs.fastq"
		InFile = open (InputFileName,'r')
		fastq_parser = SeqIO.parse(InFile, "fastq")
		def sorting (InFile):
    			for Line in InFile:
        			if any (f in Line[:30] for f in fseq):
        				if any (r in Line[-30:] for r in rseq):
        					yield Line
        			elif any (f in Line[-30:] for f in fseq):
        				if any (r in Line[:30] for r in rseq):
        					yield Line
		SeqIO.write(sorting(fastq_parser), OutFile, "fastq")
		OutFile.close()