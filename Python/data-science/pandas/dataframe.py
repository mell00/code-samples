#PANDAS DATAFRAMES#

#Create a dataframe object..:
dataframe = pd.DataFrame(data,index=index,columns=columns,dtype=dtype,copy=boolean)

#index:
#columns:
#dtype:
#copy:


    #from dictionaries of arrays:
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

    #from structured/record arrays:



    #from dictionaries of tuples:



    #from dictionaries of lists:



    #from lists of dictionaries:



    #from dictionaries of series:



    #from a series:


--------------------------------------------------------------------------------
#Create a new column
