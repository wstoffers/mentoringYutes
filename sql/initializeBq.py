#**    This line is 79 characters long.  The 80th character should wrap.   ***\

#imports:
from google.cloud import bigquery

#define:
class customBq(object):
    def __init__(self):
        self.client = bigquery.Client()
        self.dataset = None
        self.table = None

    def setUpDataset(self):
        dataset = bigquery.Dataset(f'{self.client.project}.sqlPractice')
        dataset.location = 'us-central1'
        dataset = self.client.create_dataset(dataset, timeout=30)
        self.dataset = f'{dataset.project}.{dataset.dataset_id}'

    def setUpTable(self):
        schema = [bigquery.SchemaField('id','INTEGER',mode='REQUIRED'),
                  bigquery.SchemaField('name','STRING',mode='REQUIRED'),
                  bigquery.SchemaField('michelin','INTEGER',mode='REQUIRED'),
                  bigquery.SchemaField('ace','BOOL',mode='NULLABLE'),
                  bigquery.SchemaField('error','STRING',mode='NULLABLE'),
                  bigquery.SchemaField('lookUp','BOOL',mode='NULLABLE'),
                  bigquery.SchemaField('time','TIME',mode='NULLABLE'),
                  bigquery.SchemaField('usage','STRING',mode='REPEATED')]
        table = bigquery.Table(f'{self.dataset}.problems',
                               schema = schema)
        table.clustering_fields = ['michelin']
        table = self.client.create_table(table)
        self.table = f'{table.project}.{table.dataset_id}.{table.table_id}'

#run:
if __name__ == '__main__':
    bq = customBq()
    bq.setUpDataset()
    bq.setUpTable()
