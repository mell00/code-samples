#STATISTICS WITH PANDAS#

dataframe.function() #syntax for indexing dataframe object itself
dataframe['column_name'] #syntax for indexing series (column_name) of dataframe

df = dataframe['column_name']
df[indexer] #syntax for indexing a label within a series (column_name) within a dataframe


#Count # of rows with each unique value of variable:
dataframe['column_name'].value_counts()

#Count total # of rows in dataframe:
len(dataframe)

#Count # of distinct values in column column_name:
dataframe['column_name'].nunique()

#Return basic descriptive statistics for each column (or GroupBy):
dataframe.describe()

#Return sum of values of each object:
dataframe.sum()

#Return count of non-NA/null values of each object:
dataframe.count()

#Return median value of each object:
dataframe.median()

#Return quantiles of each object:
dataframe.quantile([0.25,0.75])

#Apply function to each object:
dataframe.apply(function)

#Return minimum value of each object:
dataframe.min()

#Return maximum value of each object:
dataframe.max()

#Return mean value of each object:
dataframe.mean()

#Return variance of each object:
dataframe.var()

#Return standard deviation of each object:
dataframe.std()

#Remove rows with any column containing null data:
dataframe.dropna()

#Replace all null data with specified value:
dataframe.fillna(value)
