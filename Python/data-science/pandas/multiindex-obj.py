#MULTI-INDEX OBJECTS IN PANDAS#

#Create a multi-index object..
    #from a list of arrays:


    #from an array of tuples:


    #from a crossed set of iterables:


    #from a dataframe:


    #by passing a list of arrays directly into a series or dataframe:


m_index.get_level_values()

m_index.remove_unused_levels()

m_index.reindex()

m_index.loc()

m_index.loc(slice(None))

m_index.loc[(slice('column_1','column_2',..,'column_n'),...), :]
