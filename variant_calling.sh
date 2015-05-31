#! /bin/bash
######################################
#Author: Amy X. Guo 
#Institution: Duke University 
#Lab: Sue Jinks-Robertson Lab
######################################
echo -n "I will align all the files and perform variant calling...  :" 
while read ref; do
	echo $ref
	read sorted_input
	echo $sorted_input
	bowtie2-build $ref refseq
	bowtie2 -x refseq -U $sorted_input -S sorted_input.sam
	samtools view -b -S -o sorted_input.bam sorted_input.sam
	samtools sort sorted_input.bam sorted_input.sorted
	samtools index sorted_input.sorted.bam
	samtools mpileup -f $ref sorted_input.sorted.bam > sorted_input.mpileup
	samtools mpileup -g -f $ref sorted_input.sorted.bam > sorted_input_variants.bcf
	bcftools view -c -v sorted_input_variants.bcf > sorted_input_variants
	j=$sorted_input
# 	k=".sam"
# 	samfile=$j$k
	l=".bam"
	bamfile=$j$l
	# m=".sorted"
	# sortedfile=$j$m
	# n=".sorted.bam"
	# sortedbamfile=$j$n
	o="_variants.bcf"
	variantsbcf=$j$o
	p="_variants"
	variants=$j$p
	z=".mpileup"
	variantsmpileup=$j$z
	mv sorted_input.sam $samfile
	mv sorted_input.bam $bamfile
	# mv SGDF14R16.sorted $sortedfile
	# mv SGDF14R16.sorted.bam $sortedbamfile
	mv sorted_input_variants.bcf $variantsbcf
	mv sorted_input_variants $variants
	mv sorted_input.mpileup $variantsmpileup
done