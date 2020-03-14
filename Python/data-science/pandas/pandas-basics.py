#PANDAS BASICS#

import numpy as np
import pandas as pd

#Pandas utilizes three main types of data structure objects: series, indexes, and dataframes.
-----------------------------------------------------------------------------------------------
#Series
#Create a series object:
series = pd.Series(data,index=index,dtype=dtype,name=name,copy=boolean,fastpath=boolean)
#example #1:
series = pd.Series([1,2,3,4,5])
#calling series..
series
#will return the following:
0     1
1     2
2     3
3     4
4     5
dtype: int64
#where the digits in the left-most column are index values, and those in the right-most column are the corresponding array values.

#example #2:
series = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
#calling series..
series
#returns the following:
0     #some random number#
1     #some random number#
2     #some random number#
3     #some random number#
4     #some random number#
dtype: float64

-----------------------------------------------------------------------------------------------
#Indexes
#Create an index object:
index = pd.Index(data,dtype=dtype,copy=boolean,name=object_name,tuplelze_cols=boolean)
#example #1:
index = pd.Index([1,2,3])
#will return:
Int64Index([1,2,3],dtype='int64')

#example #2:
index = pd.Index(list('abc'))
#will return:
Index(['a','b','c'],dtype='object')
-----------------------------------------------------------------------------------------------
#Dataframes
#Create a dataframe object:
dataframe = pd.DataFrame(data,index=index,columns=columns,dtype=dtype,copy=boolean)
#example #1 (contruction of a dataframe from a dictionary):
d = {'column_1':[1,2,3],'column_2':[4,5,6],'column_3':[7,8,9]}
dataframe = pd.DataFrame(data=d)
#calling dataframe..
dataframe
#will return:
       column_1   column_2   column_3
0         1          4          7
1         2          5          8
2         3          6          9
dtype: int64

#example #2 (construction of a dataframe from a numpy ndarray):
dataframe = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]),columns=['column_1','column_2','column_3'])
#calling dataframe..
dataframe
#will return:
       column_1   column_2   column_3
0         1          4          7
1         2          5          8
2         3          6          9
dtype: int64
