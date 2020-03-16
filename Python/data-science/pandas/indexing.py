#PANDAS INDEXING#

#Basic indexing by object type:
series['label'] #index series by label, returning a scalar value
frame['column_name'] #index dataframe by series corresponding to column_name, returning the series
frame[['column_name1','column_name2']] #index dataframe by list of series corresponding to column_name1 and column_name2, returning both series

#Basic dataframe indexing using the above syntax:
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

d = dataframe['column_1']

d[0]
#will return:
1

#Multiple column indexing example:
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

dataframe[['column_1','column_2']]
#will return:
       column_1   column_2
0         1          4
1         2          5
2         3          6
dtype: int64
--------------------------------------------------------------------------------
#Selection..
    #by attribute:
    series.label
    dataframe.column_name

    #by row slicing:
    dataframe[sliced_out_index1:sliced_out_index_2]
    OR
    dataframe[::sliced_out_index_count]

    #by label:
    dataframe.loc['label']
    OR
    dataframe.loc[['array','of','labels']]
    OR
    dataframe.loc['slice_with':'labels']
    OR
    dataframe.loc['conditional'] >/</<=/>= value
    OR
    dataframe.loc[callable_single_arg_function]
--------------------------------------------------------------------------------
#Selection methods:

dataframe.isin(array_or_dict)

dataframe.where(booln_cond_statemt)

dataframe.query(booln_cond_statemt_or_expression)

dataframe.duplicated()

dataframe.drop_duplicates()

dataframe.get()

dataframe.lookup()

dataframe.reindex()
