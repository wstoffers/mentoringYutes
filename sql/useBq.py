#**    This line is 79 characters long.  The 80th character should wrap.   ***\

#imports:
import sys
import os
from google.cloud import bigquery

#define:
class existingBq(object):
    def __init__(self):
        self.client = bigquery.Client()
        self.table = f'{self.client.project}.sqlPractice.problems'

    @classmethod
    def updateBq(cls, dataframe, schema):
        '''Refactor this, as laziness is not a good excuse for inappropriate
        class method usage'''
        cls = cls()
        config = bigquery.LoadJobConfig(schema=schema,
                                        write_disposition="WRITE_TRUNCATE")
        job = cls.client.load_table_from_dataframe(dataframe,
                                                   cls.table,
                                                   job_config=config)
        job.result()

#run:
if __name__ == '__main__':
    home = os.path.abspath(os.path.dirname(sys.argv[0])) 
    
