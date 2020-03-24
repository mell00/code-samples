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
    







#Select columns
