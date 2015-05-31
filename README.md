# SJR_SMRTseq
Sort,align,variant calling

SJR_SmrtSeqTool is a pipeline that sorts next-gen sequencing fastq files obtained from PACBIO platform by barcodes and aligns the barcode-sorted sequences to a reference sequence. The pipeline also identifies variants after sequence alignment.

  - Sequence alignment and variant calling using Bowtie 2 and SAMtools/Bcftools.

### Version
1.0.0

### Tech

SJR_SmrtSeqTool uses a number of open source projects to work properly:

* [Bowtie 2] - fast and sensitive read alignment
* [Bcftools] -  utilities for variant calling and manipulating VCFs and BCFs
* [SAMtools] - for storing large nucleotide sequence alignments

### Installation
The scripts are available at https://github.com/jinksrobertson/SJR_SMRTseq.git . To run the scripts, Bowtie 2 and SAMtools/Bcftools are required to be installed. See corresponding websites listed above for installation instrucitons.


### Using
The following files have to be supplied by the user and stored in the same directory as the SJR_SmrtSeqTool pipeline.
* ForBar.txt (forward barcodes, see format in sample_files)
* RevBar.txt (reverse barcodes, see format in sample_files)
* ref.txt (reference sequence, see format in sample_files)
* ccs.fastq (fastq files from PACBIO, NOTE: make sure to rename the file to "ccs.fastq")

To run the script:
```sh
$ bash sjrcan1.sh
```
Output file: "variants.txt" summarizing variants for each barcoded-sorted file.

To view individual alignement using SAMtool tview:
```sh
$ bash tview.sh
```


License
----

Duke University


**Free Software**

[SAMtools]:http://samtools.sourceforge.net
[Bcftools]:http://samtools.github.io/bcftools/
[Bowtie 2]:http://bowtie-bio.sourceforge.net/bowtie2/index.shtml



