# Counting the number of occurences per cdr3 length

import os
import csv
import pandas as pd

count = {}
count_l={}

with open('KIRV010PB-CDR3.csv') as fin, open('KIRV010PB-CDR3-counted.csv', 'w') as fout:
    for line in fin:
        ls = line.strip().split(',')
        if ls[0] not in count:
            count[ls[0]] = 0
        count[ls[0]] += 1
        
    fin.seek(0,0)

    for line in fin:
        ls = line.strip().split(',')
        if ls[1] not in count_l:
            count_l[ls[1]] = 0
        count_l[ls[1]] += 1
        
    fin.seek(0,0)
    FIRST = True
    
    for line in fin:
        if FIRST:
            fout.write('heavycdr3,lightcdr3,count-heavy,count-light\n')
            FIRST = False
        else:
            ls = line.strip().split(',')
            fout.write(line.strip() + ',' + str(count[ls[0]]) + ',' + str(count_l[ls[1]]) + '\n')
