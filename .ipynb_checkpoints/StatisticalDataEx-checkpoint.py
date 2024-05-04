import seaborn as sns
import  matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv('C:\Users\HP\Documents\Technical Programming 2\dataset - 2020-09-24.csv')

#Applying the default theme
sns.set_theme()
sns.set_style("whitegrid")
sns.lineplot(x="Nationality", y="Losses", data=df)
plt.show()




