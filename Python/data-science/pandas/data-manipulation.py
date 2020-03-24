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

    #Append rows of dataframes:
    pd.concat([df1,df2])

    #Append columns of dataframes:
    pd.concat([df1,df2],axis=1)

    #Gather columns into rows:
    pd.melt(df)

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
