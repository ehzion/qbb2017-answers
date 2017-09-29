Commands for Week 3 Homework:

-- tar xfv BYxRM_subset.tar.xv

-- twobittoFA sacCer3.2bit sacCer3.fa

-- bwa index sacCer3.fa

-- bwa mem -R '@RG\tID:##\tSM:##' sacCer3.fa A01_"##".fastq > A01_"##".sam

-- samtools view -bS A01_"##".sam | samtools sort - -o A01_"##".bam

-- freebayes -f sacCer3.fa A01_09.bam A01_11.bam A01_23.bam A01_24.bam A01_27.bam A01_31.bam A01_35.bam A01_39.bam A01_62.bam A01_63.bam > freebayes.vcf

-- vcffilter -f "QUAL > 100" freebayes.vcf > freebayesfiltered.vcf

-- ./histogram.py freebayesfiltered.vcf histogram

-- snpEff R64-1-1.86 freebayesfiltered.vcf > snpEff.out 

-- tail -n+83 freebayesfiltered.vcf > freebayesfiltered2.vcf

-- sort -k 6 -r -n freebayesfiltered2.vcf > freebayesfiltersort.vcf

-- cat freebayesfiltersort.vcf | head -5 > freebayesfiltersort5.vcf

