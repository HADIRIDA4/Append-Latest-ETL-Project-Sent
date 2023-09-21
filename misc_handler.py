import os
from lookups import SQLTablesToReplicate

def retreive_sql_file(sql_command_directory_path):
  sql_files = [sqlfile for sqlfile in os.listdir(sql_command_directory_path) if sqlfile.endswith('.sql')]
  sorted_sql_files =  sorted(sql_files) 
  return sorted_sql_files 
def return_tables_by_schema(schema_name):
    schema_tables = list()
    tables = [table.value for table in SQLTablesToReplicate]
    for table in tables:
        if table.split('.')[0] == schema_name:
            schema_tables.append(table.split('.')[1])
    return schema_tables