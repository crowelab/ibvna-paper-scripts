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
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
# %matplotlib inline

# +
KIRV7_OL=pd.read_csv('KIRV007-overlaps-CDR3-counted-LC.csv')
KIRV7_BM=pd.read_csv('KIRV007BM-CDR3-counted-LC.csv')
KIRV7_PB=pd.read_csv('KIRV007PB-CDR3-counted-LC.csv')

KIRV7_OL.head()

# +
plt.figure(figsize=(30,30))
sns.set(font_scale=1.5)
sns.set_style("white")

sns.distplot(KIRV7_OL['lightcdr3'], color='#8498af', label='OL')
sns.distplot(KIRV7_BM['lightcdr3'], color='#715f65', label='BM')
sns.distplot(KIRV7_PB['lightcdr3'], color='#fee2e3', label='PB')

plt.xlim(0,30)
plt.ylim(0,0.2)

# +
plt.figure(figsize=(30,30))
sns.set(font_scale=1.5)
sns.set_style("white")

sns.kdeplot(KIRV7_OL['lightcdr3'], color='#8498af', label='OL', linewidth=8, shade=True)
sns.kdeplot(KIRV7_BM['lightcdr3'], color='#715f65', label='BM', linewidth=8, shade=True)
sns.kdeplot(KIRV7_PB['lightcdr3'], color='#fee2e3', label='PB', linewidth=8, shade=True)

plt.xlim(-5,30)
plt.ylim(0,0.2)

plt.savefig('KIRV007-HC-CDR3.png')

# +
KIRV8_OL=pd.read_csv('KIRV008-overlaps-CDR3-counted-LC.csv')
KIRV8_BM=pd.read_csv('KIRV008BM-CDR3-counted-LC.csv')
KIRV8_PB=pd.read_csv('KIRV008PB-CDR3-counted-LC.csv')

KIRV8_OL.head()

# +
plt.figure(figsize=(30,30))
sns.set(font_scale=1.5)
sns.set_style("white")

sns.kdeplot(KIRV8_OL['lightcdr3'], color='#8498af', label='OL', linewidth=8, shade=True)
sns.kdeplot(KIRV8_BM['lightcdr3'], color='#715f65', label='BM', linewidth=8, shade=True)
sns.kdeplot(KIRV8_PB['lightcdr3'], color='#fee2e3', label='PB', linewidth=8, shade=True)

plt.xlim(-5,30)
plt.ylim(0,0.2)

# plt.legend(prop={'size': 20})
# plt.title('CDR3 Lenth Distribution', fontsize=20)
# plt.xlabel('CDR3 Length', fontsize=15)
# plt.ylabel('Frequency', fontsize=15)

plt.savefig('KIRV008-HC-CDR3.png')

# +
KIRV9_OL=pd.read_csv('KIRV009-overlaps-CDR3-counted-LC.csv')
KIRV9_BM=pd.read_csv('KIRV009BM-CDR3-counted-LC.csv')
KIRV9_PB=pd.read_csv('KIRV009PB-CDR3-counted-LC.csv')

KIRV9_OL.head()

# +
plt.figure(figsize=(30,30))
sns.set(font_scale=1.5)
sns.set_style("white")

sns.kdeplot(KIRV9_OL['lightcdr3'], color='#8498af', label='OL', linewidth=8, shade=True)
sns.kdeplot(KIRV9_BM['lightcdr3'], color='#715f65', label='BM', linewidth=8, shade=True)
sns.kdeplot(KIRV9_PB['lightcdr3'], color='#fee2e3', label='PB', linewidth=8, shade=True)

plt.xlim(-5,30)
plt.ylim(0,0.2)

# plt.legend(prop={'size': 20})
# plt.title('CDR3 Lenth Distribution', fontsize=20)
# plt.xlabel('CDR3 Length', fontsize=15)
# plt.ylabel('Frequency', fontsize=15)

plt.savefig('KIRV009-HC-CDR3.png')

# +
KIRV10_OL=pd.read_csv('KIRV010-overlaps-CDR3-counted-LC.csv')
KIRV10_BM=pd.read_csv('KIRV010BM-CDR3-counted-LC.csv')
KIRV10_PB=pd.read_csv('KIRV010PB-CDR3-counted-LC.csv')

KIRV10_OL.head()

# +
plt.figure(figsize=(30,30))
sns.set(font_scale=1.5)
sns.set_style("white")

sns.kdeplot(KIRV10_OL['lightcdr3'], color='#8498af', label='OL', linewidth=8, shade=True)
sns.kdeplot(KIRV10_BM['lightcdr3'], color='#715f65', label='BM', linewidth=8, shade=True)
sns.kdeplot(KIRV10_PB['lightcdr3'], color='#fee2e3', label='PB', linewidth=8, shade=True)

plt.xlim(-5,30)
plt.ylim(0,0.2)

# plt.legend(prop={'size': 20})
# plt.title('CDR3 Lenth Distribution', fontsize=20)
# plt.xlabel('CDR3 Length', fontsize=15)
# plt.ylabel('Frequency', fontsize=15)

plt.savefig('KIRV010-HC-CDR3.png')
# -


