#PANDAS INDEXES#

#Create an index object:
index = pd.Index(data,dtype=dtype,copy=boolean,name=object_name,tuplelze_cols=boolean)

#dtype:
#copy:
#name:
#tuplelze_cols:


#example #1:
index = pd.Index([1,2,3])
#will return:
Int64Index([1,2,3],dtype='int64')

#example #2:
index = pd.Index(list('abc'))
#will return:
Index(['a','b','c'],dtype='object')
