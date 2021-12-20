import os
import matplotlib.pyplot as plt
import pandas
import seaborn as sns
import numpy as np
import pandas as pd

# you just need edit this variable
###################################################
# plotString = 'evalSuccessRate'
# plotTitle = 'success rate curve during the evaluation'
# Xlabel = 'eval episodes'
# Ylabel = 'average success rate'

###################################################
plotString = 'evalMean'
plotTitle = 'return curve during the evaluation'
Xlabel = 'eval episodes'
Ylabel = 'average return'

####  the following codes don't need to edit  #####
df = pandas.DataFrame([])
nameList = []

names = os.listdir('./')
for name in names:
    if name.startswith(plotString):
        # plotList.append(np.load(name))
        plotArray = np.load(name)
        df_tmp = pd.DataFrame(plotArray).melt(var_name=Xlabel, value_name=Ylabel)
        df_tmp[Xlabel] = range(len(df_tmp))
        nameList = name.split("_")
        df_tmp.insert(loc=df_tmp.shape[1], column='seed', value=nameList[-1].strip('.npy'))
        df_tmp.insert(loc=df_tmp.shape[1], column='gamma', value=nameList[-2].strip('gammma'))
        # df = df.append(df_tmp)
        df = pd.concat([df, df_tmp])

df = df.reset_index()
sns.lineplot(data=df, x=Xlabel, y=Ylabel, hue='gamma', hue_order=['0.95', '0.6', '0.0'])
plt.title(plotTitle)
plt.xlabel(Xlabel)
plt.ylabel(Ylabel)
plt.legend(loc=4)
plt.savefig('./figures/{}'.format(plotTitle))


