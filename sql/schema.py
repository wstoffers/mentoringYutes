#**    This line is 79 characters long.  The 80th character should wrap.   ***\

#imports:
from google.cloud import bigquery

#define:
schema = [bigquery.SchemaField('id','INTEGER',mode='REQUIRED'),
          bigquery.SchemaField('name','STRING',mode='REQUIRED'),
          bigquery.SchemaField('michelin','INTEGER',mode='REQUIRED'),
          bigquery.SchemaField('ace','BOOL',mode='NULLABLE'),
          bigquery.SchemaField('error','STRING',mode='NULLABLE'),
          bigquery.SchemaField('lookUp','BOOL',mode='NULLABLE'),
          bigquery.SchemaField('time','TIME',mode='NULLABLE'),
          bigquery.SchemaField('usage','STRING',mode='REPEATED')]

#run:
if __name__ == '__main__':
    pass
