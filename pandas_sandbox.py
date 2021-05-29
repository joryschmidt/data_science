import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

# labels = ['a', 'b', 'c']
# my_data = [10, 20, 30]
# arr = np.array(my_data)
# d = { 'A':[1,2,np.nan], 'B':[5, np.nan, np.nan], 'C':[1,2,3] }

# series = pd.Series(data=my_data, index=labels)
# series2 = pd.Series(arr, labels)
# series3 = pd.Series(d)

# ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])
# ser2 = pd.Series([1,2,5,4], ['USA', 'Germany', 'Italy', 'Japan'])
# ser3 = pd.Series(data=labels)
# print(ser1 + ser2)

# df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
# df['X + Y'] = df['X'] + df['Y']
# print(df[['X', 'Y', 'X + Y']])
# # return X and Y columns where W column is greater than 0 and Y is greater than 1
# # | instead of & for or, parenthesis seperating each boolean dataframe is necessary
# print(df[(df['W'] > 0) & (df['Y'] > 1)])
# print(df)
# df[df<0] = 0
# print(df)

# new_indexes = 'CA NY WY OR CO'.split()
# df['States'] = new_indexes
# df.set_index('States', inplace=True)
# print(df)

# outside = ['G1','G1','G1','G2','G2','G2']
# inside = [1,2,3,1,2,3]
# hier_index = list(zip(outside, inside))
# hier_index = pd.MultiIndex.from_tuples(hier_index)

# df = pd.DataFrame(randn(6,2), hier_index, ['A', 'B'])
# df.index.names = ['Groups', 'Number']
# print(df.xs(1, level='Number'))

# df = pd.DataFrame(d)
# print(df)
# print(df.dropna(thresh=2))
# df['A'].fillna(value=df['A'].mean(), inplace=True)
# print(df.fillna(value='FILL ME'))


# data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
#         'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
#         'Sales':[200,120,340,124,243,350]}
# df = pd.DataFrame(data)
# print(df)
# grouped_by_company = df.groupby('Company')
# print(grouped_by_company.sum())
# print(grouped_by_company.describe().transpose())



# Concatenating, joining, merging etc
# """
# df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
#                     'B': ['B0', 'B1', 'B2', 'B3'],
#                     'C': ['C0', 'C1', 'C2', 'C3'],
#                     'D': ['D0', 'D1', 'D2', 'D3']},
#                     index=[0, 1, 2, 3])
# df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
#                     'B': ['B4', 'B5', 'B6', 'B7'],
#                     'C': ['C4', 'C5', 'C6', 'C7'],
#                     'D': ['D4', 'D5', 'D6', 'D7']},
#                     index=[4, 5, 6, 7]) 
# df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
#                     'B': ['B8', 'B9', 'B10', 'B11'],
#                     'C': ['C8', 'C9', 'C10', 'C11'],
#                     'D': ['D8', 'D9', 'D10', 'D11']},
#                     index=[8, 9, 10, 11])
# print(pd.concat([df1, df2, df3]))
# print(pd.concat([df1, df2, df3], axis=1))
# left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                      'key2': ['K0', 'K1', 'K0', 'K1'],
#                      'A': ['A0', 'A1', 'A2', 'A3'],
#                      'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                       'key2': ['K0', 'K0', 'K0', 'K0'],
#                       'C': ['C0', 'C1', 'C2', 'C3'],
#                       'D': ['D0', 'D1', 'D2', 'D3']})    
# print(pd.merge(left, right, how='inner', on='key'))
# print(pd.merge(left, right, on=['key', 'key2']))
# """


# df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
# print(df)
# print(df['col2'].nunique())
# print(df['col2'].apply(lambda x:x*2))
# print(df.sort_values('col2'))
# print(df.isnull())


# # Pivot tables
# data = {'A':['foo','foo','foo','bar','bar','bar'],
#         'B':['one','one','two','two','one','one'],
#         'C':['x','y','x','y','x','y'],
#         'D':[1,3,2,5,4,1]}
# df = pd.DataFrame(data)
# # print(df)
# pivot = df.pivot_table(values='D', index=['A', 'B'], columns=['C'])
# print(pivot)

