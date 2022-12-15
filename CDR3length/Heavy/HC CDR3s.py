import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

KIRV7_OL=pd.read_csv('KIRV007-overlaps-CDR3-counted-HC.csv')
KIRV7_BM=pd.read_csv('KIRV007BM-CDR3-counted-HC.csv')
KIRV7_PB=pd.read_csv('KIRV007PB-CDR3-counted-HC.csv')

KIRV7_OL.head()

# +
plt.figure(figsize=(30,30))
sns.set(font_scale=1.5)
sns.set_style("white")

sns.kdeplot(KIRV7_OL['heavycdr3'], color='#8498af', label='OL', linewidth=8, shade=True)
sns.kdeplot(KIRV7_BM['heavycdr3'], color='#715f65', label='BM', linewidth=8, shade=True)
sns.kdeplot(KIRV7_PB['heavycdr3'], color='#fee2e3', label='PB', linewidth=8, shade=True)

plt.xlim(0,40)
plt.ylim(0,0.2)

plt.savefig('KIRV007-HC-CDR3.png')

KIRV8_OL=pd.read_csv('KIRV008-overlaps-CDR3-counted-HC.csv')
KIRV8_BM=pd.read_csv('KIRV008BM-CDR3-counted-HC.csv')
KIRV8_PB=pd.read_csv('KIRV008PB-CDR3-counted-HC.csv')

KIRV8_OL.head()

plt.figure(figsize=(30,30))
sns.set(font_scale=1.5)
sns.set_style("white")

sns.kdeplot(KIRV8_OL['heavycdr3'], color='#8498af', label='OL', linewidth=8, shade=True)
sns.kdeplot(KIRV8_BM['heavycdr3'], color='#715f65', label='BM', linewidth=8, shade=True)
sns.kdeplot(KIRV8_PB['heavycdr3'], color='#fee2e3', label='PB', linewidth=8, shade=True)

plt.xlim(0,40)
plt.ylim(0,0.2)

plt.savefig('KIRV008-HC-CDR3.png')

KIRV9_OL=pd.read_csv('KIRV009-overlaps-CDR3-counted-HC.csv')
KIRV9_BM=pd.read_csv('KIRV009BM-CDR3-counted-HC.csv')
KIRV9_PB=pd.read_csv('KIRV009PB-CDR3-counted-HC.csv')

KIRV9_OL.head()

plt.figure(figsize=(30,30))
sns.set(font_scale=1.5)
sns.set_style("white")

sns.kdeplot(KIRV9_OL['heavycdr3'], color='#8498af', label='OL', linewidth=8, shade=True)
sns.kdeplot(KIRV9_BM['heavycdr3'], color='#715f65', label='BM', linewidth=8, shade=True)
sns.kdeplot(KIRV9_PB['heavycdr3'], color='#fee2e3', label='PB', linewidth=8, shade=True)

plt.xlim(0,40)
plt.ylim(0,0.2)

plt.savefig('KIRV009-HC-CDR3.png')

KIRV10_OL=pd.read_csv('KIRV010-overlaps-CDR3-counted-HC.csv')
KIRV10_BM=pd.read_csv('KIRV010BM-CDR3-counted-HC.csv')
KIRV10_PB=pd.read_csv('KIRV010PB-CDR3-counted-HC.csv')

KIRV10_OL.head()

plt.figure(figsize=(30,30))
sns.set(font_scale=1.5)
sns.set_style("white")

sns.kdeplot(KIRV10_OL['heavycdr3'], color='#8498af', label='OL', linewidth=8, shade=True)
sns.kdeplot(KIRV10_BM['heavycdr3'], color='#715f65', label='BM', linewidth=8, shade=True)
sns.kdeplot(KIRV10_PB['heavycdr3'], color='#fee2e3', label='PB', linewidth=8, shade=True)

plt.xlim(0,40)
plt.ylim(0,0.2)

plt.savefig('KIRV010-HC-CDR3.png')
