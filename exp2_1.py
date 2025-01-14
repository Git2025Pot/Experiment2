import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/Git2025Pot/Experiment2/refs/heads/main/insurance.csv');
df.drop(['name'],axis=1,inplace=True);
ohed = pd.get_dummies(df,columns=['insu_status']);

lst=['age','salary','insu_status']
df = df[lst];

x = df['age'];
y = df['insu_status'];
plt.scatter(x,y);
plt.xlabel('age');
plt.ylabel('Insurance status');
plt.show();
