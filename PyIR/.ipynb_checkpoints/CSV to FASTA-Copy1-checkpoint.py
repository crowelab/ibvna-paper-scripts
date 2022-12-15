# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import sys
import pandas as pd
import numpy as np
import os
import re
import subprocess
import csv
import gzip
import json
import bson
#import argparse

#parser = argparse.ArgumentParser()


files = ['KIRV-LC.csv']
# -

#df= pd.read_excel('04.05.2017_Nigeria_DRC_EBOV Seq_1_.xlsx', sheetname='Sheet1')
with open('KIRV-LC.fasta', 'w') as fout:
    for f in files:
        with open(f,'r') as fin, open(f.split('.')[0] + '.fasta', 'w') as fout:
            reader = csv.DictReader(fin)
            for row in reader:
                fout.write('>' + row['ID'] + '\n')
                fout.write(row['LC'] + '\n')


# +
#df.head()

# +
#d=df.to_dict()
#print(d['Ab ID'])
#print (d.keys())

# +
#with open('Nigeria1.fasta', 'w') as fout: 
#    for key in d:
#        fout.write('>' + d[key]['Ab ID'] + '\n')
#        fout.write(d[key]['Heavy Sequence'] + '\n')
# -


