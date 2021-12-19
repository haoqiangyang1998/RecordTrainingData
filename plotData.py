import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# you just need edit this variable
plotString = 'success'

####  the following codes don't need to edit  #####
plotList = []

names = os.listdir('./')
for name in names:
    if name.startswith(plotString):
        plotList.append(np.load(name))

plotArray = np.array(plotList)
df = pd.DataFrame(plotArray).melt(var_name='episode', value_name='success rate')
sns.lineplot(x='episode', y='success rate', data=df)
plt.title(plotString)
plt.savefig('./figures/{}'.format(plotString))


