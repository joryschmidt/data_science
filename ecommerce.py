import pandas as pd

ecom = pd.read_csv('data/ecommerce.csv')
# print(df)

# print(ecom.describe())
# print(ecom.info())

# print(ecom['Purchase Price'].mean())
# print(ecom['Purchase Price'].max())
# print(ecom['Purchase Price'].min())

# print(ecom[ecom['Language'] == 'en'].shape[0])
# print(ecom[ecom['Job'] == 'Lawyer'].shape[0])
print(ecom.groupby('AM or PM'))
