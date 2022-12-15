
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

KIRV7=pd.read_csv('KIRV007SHMCDR3.csv')
KIRV7.head()

g = sns.catplot(x='Chain', y='heavy_percent_id', hue='Sample',
               data=KIRV7, kind="violin", linewidth=14, linecolor='black', palette=['#715f65','#fee2e3','#8498af'])
g.fig.set_figwidth(60)
g.fig.set_figheight(30)
g.set(ylim=(60, 110))

g.savefig("KIRV7SHM.png")

KIRV8=pd.read_csv('KIRV008SHMCDR3.csv')
KIRV8.head()

g = sns.catplot(x='Chain', y='heavy_percent_id', hue='Sample',
               data=KIRV8, kind="violin", linewidth=14, linecolor='black', palette=['#715f65','#fee2e3','#8498af'])
g.fig.set_figwidth(60)
g.fig.set_figheight(30)
g.set(ylim=(60, 110))

g.savefig("KIRV8SHM.png")

KIRV9=pd.read_csv('KIRV009SHMCDR3.csv')
KIRV9.head()

g = sns.catplot(x='Chain', y='heavy_percent_id', hue='Sample',
               data=KIRV9, kind="violin", linewidth=14, linecolor='black', palette=['#715f65','#fee2e3','#8498af'])
g.fig.set_figwidth(60)
g.fig.set_figheight(30)
g.set(ylim=(60, 110))

g.savefig("KIRV9SHM.png")

KIRV10=pd.read_csv('KIRV010SHMCDR3.csv')
KIRV10.head()

g = sns.catplot(x='Chain', y='heavy_percent_id', hue='Sample',
               data=KIRV10, kind="violin", linewidth=14, linecolor='black', palette=['#715f65','#fee2e3','#8498af'])
g.fig.set_figwidth(60)
g.fig.set_figheight(30)
g.set(ylim=(60, 110))

g.savefig("KIRV10SHM.png")
