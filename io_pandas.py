import numpy as np
import pandas as pd

df = pd.read_csv('data/example.csv')
# print(df)
# df.to_csv('data/example_output.csv', index=False)

# df = pd.read_excel('data/Excel_Sample.xlsx', sheet_name='Sheet1')
# print(df)
# df.to_excel('data/example_excel.xlsx', sheet_name='NewSheet')

# # Read tables from html link
# data = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
# data = np.array(data)
# columns = ['Bank Name', 'City', 'State', 'Cert', 'Acquiring Inst.', 'Closing Date', 'Fund']
# df = pd.DataFrame(data[0], columns=columns)
# print(df)
# df.to_csv('data/failed_banks.csv', index=False)

# # interface pandas with sqlite
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///:memory:')
# df.to_sql('my_table', engine)
# sqldf = pd.read_sql('my_table', con=engine)
# print(sqldf)
