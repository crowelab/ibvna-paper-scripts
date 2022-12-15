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

FASTA = 'HC.fasta'
CSV = 'HC.csv'

outrows = []

with open(FASTA, 'r') as fin:
    for line in fin:
        seqstring = line[1:].strip() + ',' #Grab everything after the first character, which will be a '>' in a proper fasta file
        seqstring += fin.readline()
        outrows.append(seqstring)
    
with open(CSV,'w') as fout:
    fout.write('Label,Sequence\n')
    for line in outrows:
        fout.write(line)
# -


