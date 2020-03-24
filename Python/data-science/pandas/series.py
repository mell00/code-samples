#PANDAS SERIES#

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
