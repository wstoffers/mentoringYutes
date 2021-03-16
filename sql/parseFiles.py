#**    This line is 79 characters long.  The 80th character should wrap.   ***\

#imports:
import sys
import os
from pathlib import Path
import re
import numpy as np
import pandas as pd
import pyarrow
from google.cloud import bigquery

sys.path.append(os.environ.get('CIPHERPATH'))
exec(f"from {os.environ.get('CIPHERMODULE')} import cipher")
from schema import schema
from useBq import existingBq

#define:
def collect(directory):
    '''Collects desired *.sql files out of magnolia/, everest/, and hyotei/'''
    holdsSql = ['magnolia','everest','hyotei']
    keep = {}
    for path, directories, files in os.walk(directory):
        if os.path.split(path)[1] in holdsSql:
            keep[path] = [x for x in files if re.match('[0-9]+-.*sql$',x)]
    #order each group by file modification time:
    for group in keep:
        keep[group] = sorted(keep[group],
                             key=lambda k:Path(os.path.join(group,
                                                            k)).stat().st_mtime)
    return keep

def ceilingDivide(x):
    return -(-x//4)

def parse(keep):
    frame = []
    toMatch = re.compile('(^[0-9]+)-(.*)\.sql$')
    for path in keep:
        sqls = keep[path]
        if sqls:
            for sql in sqls:
                matched = toMatch.search(sql)
                row = [int(cipher().decreaseDifficulty(matched.group(1))),
                       matched.group(2),
                       3-ceilingDivide(12%len(os.path.split(path)[1])),
                       None,
                       np.nan,
                       None,
                       pd.Timedelta(0),
                       usageArray(os.path.join(path,sql))]
                frame.append(row)
    return frame

def usageArray(filePath):
    '''Extracts all uppercase words, functions, and phrases'''
    with open(filePath) as sql:
        cleaned = re.sub('".*"','',sql.read())
        groups = re.findall('[A-Z ]+',cleaned)
    return [x.strip() for x in groups if x.strip()]

def combine(wholeFrame):
    whole = pd.DataFrame(wholeFrame,columns=[x.name for x in schema])
    parent = os.path.dirname(os.environ.get('CIPHERPATH'))
    path = os.path.join(parent,'test.csv')#'sqlMetadata.csv')
    partial = pd.read_csv(path,true_values=['t'],
                               false_values=['f'],
                               parse_dates=['time'],
                               date_parser=lambda k: pd.to_timedelta(k),
                               skipinitialspace=True)
    whole = whole.set_index('id')
    partial = partial.set_index('id')
    whole.update(partial)
    whole = whole.reset_index()
    return whole

#run:
if __name__ == '__main__':
    home = os.path.abspath(os.path.dirname(sys.argv[0])) 
    sqls = collect(home)
    frame = parse(sqls)
    dataFrame = combine(frame)
    existingBq.updateBq(dataFrame, schema)
