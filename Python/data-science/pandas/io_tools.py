#PANDAS I/O TOOLS#

dataframe = pd.DataFrame(data,index=index,columns=columns,dtype=dtype,copy=boolean)

#pandas native (file path):
dataframe.read_table()
pd.read_fwf()
dataframe.read_clipboard()

#CSV (text):
pd.read_csv()
dataframe.to_csv()

#JSON (text):
pd.read_json()
pd.json_normalize()
dataframe.build_table_schema()

#Excel (cells):
dataframe.read_excel()
dataframe.Excelfile.parse()
with ExcelWriter('file_path.xlsx') as writer:
    dataframe.to_excel(writer)

#HTML (string containing <table></table):
pd.read_html(url)

#SQL (query or database table):
pd.read_sql_table('table_name',..)
pd.read_sql_query(sql,con[index_col,..])
pd.read_sql(sql,con[index_col,..])

#STATA:
pd.read_stata('file_path')
