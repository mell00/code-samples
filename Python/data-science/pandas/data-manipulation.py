#DATA MANIPULATION IN PANDAS#

#Reshape layout of data set
    #Order rows by column (column_name) values (low -> high):
    df.sort_values('column_name')

    #Order rows by column (column_name) values (high -> low):
    df.sort_values('column_name',ascending=False)

    #Rename columns of a dataframe (df):
    df.rename(columns={'new_column_name':'current_column_name'})

    
