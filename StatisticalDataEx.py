import seaborn as sns
import  matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv('C:\\Users\\HP\\Documents\\Technical Programming 2\\dataset - 2020-09-24.csv')

#Applying the default theme
sns.set_theme()

#DEMOSTRATION OF SETTING AESTHETIC STYLE
sns.set_style("whitegrid")
#Setting the context to "talk" for larger plots suitable for presentations
sns.set_context("talk")
sns.lineplot(x="Club", y="Saves", data=df)
plt.show()

#DISTRIBUTION PLOT
sns.displot(df['Losses'])
sns.kdeplot(data=df['Penalties'])


