import numpy as np
import pandas as pd

sal = pd.read_csv('data/Salaries.csv')

print(sal.head())
print(sal.info())
print(sal['BasePay'].mean())
print(sal['OvertimePay'].max())
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName'])
print(sal.loc[sal['TotalPayBenefits'].idxmax()])

group_by_year = sal.groupby('Year')
print(group_by_year.mean()['BasePay'])

print(sal['JobTitle'].nunique())
print(sal['JobTitle'].value_counts()[:5])
print(sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1))
print(sal[sal['JobTitle'].str.contains('Chief', case=False)].shape[0])
print(sal[sal['JobTitle'].str.contains('Chief', case=False)])
sal['title_length'] = sal['JobTitle'].apply(len)
print(sal[['title_length', 'TotalPayBenefits']].corr())
