import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthieu', 'Laura', 'Kevin', 'Jonas'],

'note' : [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'tentatives' : [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualifier' : ['oui', 'non', 'oui', 'non', 'non', 'oui', 'oui', 'non', 'non', 'oui']}

df= pd.DataFrame(data=exam_data , index= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(df)

df=df.dropna()
print(df)
print(df.loc[:,['name','note']])

df=df._append({'name': "Suresh", 'note': 15.5, 'tentatives': 1, 'qualifier': "yes"},ignore_index= True)
print(df)
print(df.drop(columns='tentatives'))

df['Success'] = df['note'].apply(lambda x: 1 if x > 10 else 0)
print(df)
df.to_csv('my_data.csv')