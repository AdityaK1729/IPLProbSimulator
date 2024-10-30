import pandas as pd
df=pd.read_csv('ipl_2024_matches.csv')
print(df['venue'].value_counts())