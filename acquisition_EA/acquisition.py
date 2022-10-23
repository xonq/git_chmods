#!/usr/bin/env python3
#elaine aquino

#open seq and pull sample
virdna = open('practice_ac.fastq', 'r')
virseq = ''

for line in virdna:
  line = line.rstrip()
  if line.startswith('@') == False:
    line = line.split()
    virseq = ''.join(line)
    break
print(virseq)
  
