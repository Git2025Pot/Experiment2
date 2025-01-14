import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('https://raw.githubusercontent.com/Git2025Pot/Experiment2/refs/heads/main/insurance.csv');

le = LabelEncoder()
led = le.fit_transform(df['insu_status'])
df['insu_status'] = led

lst=['age','salary','insu_status']
df = df[lst];

x = df['age'];
y = df['insu_status'];
plt.scatter(x,y);
plt.xlabel('age');
plt.ylabel('Insurance status');
plt.show();
