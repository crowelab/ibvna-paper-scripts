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

import pandas as pd

df = pd.read_csv('DAVIDHO-paired (1).csv')

df.head()

df_h = df.sort_values(by=["heavy_v_gene", "heavy_j_gene", "heavy_cdr3_aa_length"])
df_l = df.sort_values(by=["light_v_gene", "light_j_gene", "light_cdr3_aa_length"])

df_h.head()

df_l.head()

# +
f = open('COV2_heavy.dat', 'w')

last_v = ""
last_j = ""
last_cdr3len = -1
last_end = False

for index,row in df_h.iterrows():

    v = str(row['heavy_v_gene'])
    j = str(row['heavy_j_gene'])
    cdr3len = str(row['heavy_cdr3_aa_length'])
    cdr3_nt = str(row['heavy_cdr3_(dna)'])
    if cdr3_nt.find('-') != -1:
        continue
    vdj = str(row['heavy_nt_trimmed']).replace("-","")

    if last_cdr3len == -1:
        last_v = v
        last_j = j
        last_cdr3len = cdr3len
    elif (last_v!=v or last_j!=j or last_cdr3len!=cdr3len):
        if last_end == False:
            f.write("END\n")
            #last_end = True
        #else:
        #    last_end = False
    
    raw_iso = str(row['heavy_isotype'])
    if raw_iso.find('IGHG')!=-1:
        iso = "IgG"
    elif raw_iso.find('IGHM')!=-1:
        iso = "IgM"
    elif raw_iso.find("IGHA")!=-1:
        iso = "IgA"
    elif raw_iso.find('IGHE')!=-1:
        iso = "IgE"
    elif raw_iso.find("IGHD")!=-1:
        iso = "IgD"
    else:
        iso = "NA"

    idstr = str(row['run_id']) + "_" + str(row['sample_id']) + "_" + str(row['clonotype_id'])

    if (v=="" or j=="" or str(row['heavy_cdr3_(aa)'])=="" or cdr3_nt == "" or str(row['heavy_nt_trimmed']) == "" or str(row['heavy_percent_id']) == ""):
        print(idstr)
    
    line = idstr + " " + str(iso) + " 10x " + str(v) + " " + str(j) + " " + str(row['heavy_cdr3_(aa)']) + " " + cdr3_nt + " " + vdj + " " + str(row['heavy_percent_id'])

    #if v=="IGHV1-18" and j = 'IGHJ2'
    
    f.write(line + '\n')
    
    last_v = v
    last_j = j
    last_cdr3len = cdr3len
    
f.write("END\n")

f.close()

# +
f = open('COV2_light.dat', 'w')

last_v = ""
last_j = ""
last_cdr3len = -1
last_end = False

for index,row in df_l.iterrows():

    v = str(row['light_v_gene'])
    j = str(row['light_j_gene'])
    cdr3len = str(row['light_cdr3_aa_length'])
    cdr3_nt = str(row['light_cdr3_(dna)'])
    if cdr3_nt.find('-') != -1:
        continue
    vdj = str(row['light_nt_trimmed']).replace("-","")
    
    if last_cdr3len == -1:
        last_v = v
        last_j = j
        last_cdr3len = cdr3len
    elif (last_v!=v or last_j!=j or last_cdr3len!=cdr3len):
        if last_end == False:
            f.write("END\n")
            #last_end = True
        #else:
            #last_end = False
    
    raw_iso = str(row['light_isotype'])
    if raw_iso.find('IGK')!=-1:
        iso = "IgK"
    elif raw_iso.find('IGL')!=-1:
        iso = "IgL"
    else:
        iso = "NA"

    idstr = str(row['run_id']) + "_" + str(row['sample_id']) + "_" + str(row['clonotype_id'])
    
    line = idstr + " " + str(iso) + " 10x " + str(v) + " " + str(j) + " " + str(row['light_cdr3_(aa)']) + " " + cdr3_nt + " " + vdj + " " + str(row['light_percent_id'])

    f.write(line + '\n')
    
    last_v = v
    last_j = j
    last_cdr3len = cdr3len
    
f.write("END\n")

f.close()
# -


