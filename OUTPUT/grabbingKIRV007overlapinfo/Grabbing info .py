# 05/07/2020 
#
# I took the file that has all of the KIRV007 overlaps that seth ordered. But since his file only had sequence info and none of the additional information that comes with pyir, i grabbed that info after running dbtools to get paired.csv on all of kirv007 runs. 
#
# now we have an overlap file with all the sequence features associated. 

import csv
import os

ALLseqs='KIRV7-ALL-3.csv'
Overlaps='KIRV007overlaps.csv'

OUTFILE='KIRV007overlapswinfo.csv'
MISSING='missing.dat'

#dictionary d is going to hold my mongo ID as keys and the values is all my relevant info
d={}

with open(Overlaps, 'r')as fin: 
    reader=csv.DictReader(fin)
    #each row variable is a dictionary now
    #and we know that the keys are going to correspond to the headers in the csv trial
    
    for row in reader:
        #mongo is equal to the string value that is accessed when you look for mongo_id key in row
        #so mongo holds this string now
        mongo = row['ID']
        
        if mongo not in d:
            #this mongoID string i have is equal to this object now
            #this mongoID is now equal to row
            d[mongo] = {'row1': [], 'row2': []}
        
        # there might be multiple values for row1   
        d[mongo]['row1'].append(row)
        
        
with open(ALLseqs, 'r')as fin2, open(MISSING, 'w') as mout: 
    reader=csv.DictReader(fin2)
    for row in reader:
        if row['ID'] in d:
            d[row['ID']]['row2'].append(row)
        else:
            mout.write(row['ID'] + '\n')
# -

with open(OUTFILE, 'w') as fout:
    fout.write('ID,HC-AA,LC-AA,ID,heavy_v_gene,heavy_j_gene,heavy_isotype,heavy_cdr3_aa,heavy_cdr3_aa_length,heavy_percent_id,heavy_occurrences,heavy_mutations,heavy_d_gene,heavy_cdr3_dna,heavy_nt_trimmed,heavy_nt,heavy_aa,light_v_gene,light_j_gene,light_isotype,light_cdr3_aa,light_cdr3_aa_length,light_percent_id,light_occurrences,light_mutations,light_d_gene,light_cdr3_dna,light_nt_trimmed,light_nt,light_aa\n')
    
    for x in d:
        for row1 in d[x]['row1']:
            outstr = row1['ID'] + ',' + \
                row1['heavy_aa_trimmed'] + ',' + \
                row1['light_aa_trimmed'] + ','
            
            if len(d[x]['row2']) > 0:
                for row2 in d[x]['row2']:
                    fout.write(outstr + 
                    row2['ID'] + ',' + \
                    row2['heavy_v_gene'] + ',' + \
                    row2['heavy_j_gene'] + ',' + \
                    row2['heavy_isotype'] + ',' + \
                    row2['heavy_cdr3_aa'] + ',' + \
                    row2['heavy_cdr3_aa_length'] + ',' + \
                    row2['heavy_percent_id'] + ',' + \
                    row2['heavy_occurrences'] + ',' + \
                    row2['heavy_mutations'] + ',' + \
                    row2['heavy_d_gene'] + ',' + \
                    row2['heavy_cdr3_dna'] + ',' + \
                    row2['heavy_nt'] + ',' + \
                    row2['heavy_aa'] + ',' + \
                    row2['light_v_gene'] + ',' + \
                    row2['light_j_gene'] + ',' + \
                    row2['light_isotype'] + ',' + \
                    row2['light_cdr3_aa'] + ',' + \
                    row2['light_cdr3_aa_length'] + ',' + \
                    row2['light_percent_id'] + ',' + \
                    row2['light_occurrences'] + ',' + \
                    row2['light_mutations'] + ',' + \
                    row2['light_d_gene'] + ',' + \
                    row2['light_cdr3_dna'] + ',' + \
                    row2['light_nt'] + ',' + \
                    row2['light_aa'] + '\n')
            else:
                fout.write(outstr + 'N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A\n')


