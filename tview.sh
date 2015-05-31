#! /bin/bash
######################################
#Author: Amy X. Guo 
#Institution: Duke University 
#Lab: Sue Jinks-Robertson Lab
######################################

echo -n "Enter reference sequence file (e.g. F1R1.fna)and press [ENTER]:" 
read ref
echo -n "Enter barcode-sorted file (e.g. F1R1) and press [ENTER]:"
read sorted_input
bowtie2-build $ref refseq
bowtie2 -x refseq -U $sorted_input -S sorted_input.sam
samtools view -b -S -o sorted_input.bam sorted_input.sam
samtools sort sorted_input.bam sorted_input.sorted
samtools index sorted_input.sorted.bam
samtools mpileup -g -f $ref sorted_input.sorted.bam > sorted_input_variants.bcf
bcftools view -c -v sorted_input_variants.bcf > sorted_input_variants
j=$sorted_input
k=".sam"
samfile=$j$k
l=".bam"
bamfile=$j$l
o="_variants.bcf"
variantsbcf=$j$o
p="_variants"
variants=$j$p
a=".fna"
seq=$j$a
mv sorted_input.sam $samfile
mv sorted_input.bam $bamfile
mv sorted_input_variants.bcf $variantsbcf
mv sorted_input_variants $variants
samtools tview sorted_input.sorted.bam $seq

