#PANDAS DATAFRAMES#

#Create a dataframe object:
dataframe = pd.DataFrame(data,index=index,columns=columns,dtype=dtype,copy=boolean)

#index:
#columns:
#dtype:
#copy:


#From dictionaries of arrays:
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

#From structured/record arrays:



#From dictionaries of tuples:



#From dictionaries of lists:



#From lists of dictionaries:



#From dictionaries of series:



#From a series:
