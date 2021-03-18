#**    This line is 79 characters long.  The 80th character should wrap.   ***\

#imports:
import os
from datetime import datetime

#define:
def changeModificationDateTime(filePath, isoDateTime):
    epochDateTime = datetime.fromisoformat(isoDateTime).timestamp()
    os.utime(filePath,(epochDateTime,epochDateTime))

#run:
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', required=True)
    parser.add_argument('--time', '-t', required=True)
    args = parser.parse_args()
    fileToChange = args.file
    newDateTime = args.time
    changeModificationDateTime(fileToChange, newDateTime)
