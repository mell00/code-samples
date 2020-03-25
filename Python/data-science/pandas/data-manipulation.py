#DATA MANIPULATION IN PANDAS#

#Reshape layout of data set
    #Order rows by column (column_name) values (low -> high):
    df.sort_values('column_name')

    #Order rows by column (column_name) values (high -> low):
    df.sort_values('column_name',ascending=False)

    #Rename columns of a dataframe (df):
    df.rename(columns={'new_column_name':'current_column_name'})

    df.sort_index()

    df.reset_index()

    df.drop(columns=['length','height'])

    #Spread rows into columns:
    df.pivot(columns='var',values='val')

    #Add rows of dataframes:
    pd.concat([df1,df2])

    #Append columns of dataframes:
    pd.concat([df1,df2],axis=1)

    #Add a single column multiplying values of existing columns:
    df['new_column']=df.existing_column1*df.existing_column2*df.existing_columnn

    #Compute and append one or more new columns:
    df.assign({'new_column':[column_val1,column_val2,..,column_valn]},index=['row_1','row_2',..,'row_n']) #dictionary of values of new_column, matched with index values (rows)
    df.assign(new_column=df['existing_column'] **kwargs) #value of 'existing_column's evaluated on df
    OR
    df.assign(new_column=lambda x: x['existing_column'] **kwargs) #value of 'existing_column's evaluated on df by substitution of variable x as df
        #NOTE: callable may be re-used for multiple columns

    #Column vector functions (operate on either one selected column or all columns):
        #Find element-wise maximum of selected column(s)
        df.max(axis=1)
        #Find element-wise minimum of selected column(s)
        df.min(axis=1)
        #Find absolute value of selected column(s)
        df.abs()
        #Trim values of selected column(s) at given input thresholds
        df.clip(lower=low_val,higher=high_val)

    #Gather columns into rows:
    pd.melt(df)

    #Combine data sets:
    pd.merge(df1,df2,how='left',on='column_n')

    pd.merge(df1,df2,how='right',on='column_n')

    pd.merge(df1,df2,how='inner',on='column_n')

    pd.merge(df1,df2,how='outer',on='column_n')

    #Filter joins:
        #Filter rows of df1 that have a match in df2
        df1[df1.column_n.isin(df2.column_n)]
        #Filter rows of df1 that do not have a match in df2
        df1[~df1.column_n.isin(df2.column_n)]

#Select rows
    #Select rows by (slice) position:
    df.iloc[1:4]

    #Select rows meeting given logical criteria, and only the columns specified:
    df.loc[logical_condition,['column_1','column_2','column_n']]

    #Extract rows meeting given logical criteria:
    df[logical_condition]

    #Select first n rows:
    df.head(n)

    #Select last n rows:
    df.tail(n)

    #Select and order top n entries:
    df.nlargest(n,'value')

    #Select and order bottom n entries:
    df.nsmallest(n,'value')

    #Randomly select n rows:
    df.sample(n=n)

    #Randomly select fraction (frac) of rows:
    df.sample(frac=frac)

    #Remove duplicate rows (only considering columns):
    df.drop_duplicates()

#Select columns
    #Select columns by (slice) position, between 'pos_1' and 'pos_2' (inclusive):
    df.loc[:,'pos_1':'pos_2']

    #Select columns by position (first column is 0):
    df.iloc[:,[val_1,val_2,val_n]]

    #Select one column with specific name:
    df['column'] OR df.column

    #Select multiple columns with specific names:
    df[['column_1','column_2','column_3']]

    #Select column(s) whose name matches regular expression 'regex':
    df.filter(regex='regex')
        #Regular expression syntax examples:
        '\.' #matches strings containing a period '.'
        'length$' #matches strings ending with the word 'length'
        '^word' #matches strings beginning with the word 'word'
        'x[1-5]' #matches strings beginning with x and ending with 1,2,3,4,5
        '(^!string)' #matches strings except the string 'string'

#Group data
    #Return a GroupBy object, grouped by values in column ('col'):
    df.groupby(by='col')

    #Return a GroupBy object, grouped by values in index level ('ind'):
    df.groupby(by='ind')

    #Return value of group size:
    df.size()

    #Return aggregated group by function:
    df.agg(function)

    #Return group with values shifted forward by 1:
    df.shift(1)

    #Return group with values shifted behind by 1:
    df.shift(-1)

    #Return ranked group by 'method' and either rescaled or not rescaled:
    df.rank(method='method',pct=boolean)

    #Return cumulative sum of group values:
    df.cumsum()

    #Return cumulative maximum value of group:
    df.cummax()

    #Return cumulative minimum value of group:
    df.cummin()

    #Return cumulative product of group values:
    df.comprod()
