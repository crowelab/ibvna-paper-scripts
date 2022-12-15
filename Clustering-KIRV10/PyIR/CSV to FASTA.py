
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

files = ['KIRV10_LC.csv']
with open('KIRV_10LC.fasta', 'w') as fout:
    for f in files:
        with open(f,'r') as fin, open(f.split('.')[0] + '.fasta', 'w') as fout:
            reader = csv.DictReader(fin)
            for row in reader:
                fout.write('>' + row['ID'] + '\n')
                fout.write(row['HC'] + '\n')
