import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%matplotlib inline

titanic_df = pd.read_excel('titanic3.xls','titanic3', index_col=None, na_values=['NA'])
#print(titanic_df.head())
#plt.figure()
#titanic_df.plot()
#print(titanic_df.describe())

few = titanic_df.drop(['ticket','cabin','boat','body','fare'],axis=1).head()
#print(few)
few.plot.bar()
print(titanic_df.isnull().sum())

#pd.value_counts(titanic_df['survived']).plot.bar()
pd.value_counts(titanic_df['sex']).plot.bar()
# print(type(x))sex
plt.show()
#plott = x.plot.bar()
#print(plott)

# def plott1():
#     plt.plot([1, 2, 3, 4])
#     plt.ylabel('some numbers')
#     plt.show()
#
# def plott2():
#     plt.plot(x)
#     plt.show()
#
# plott1()
# plott2()
