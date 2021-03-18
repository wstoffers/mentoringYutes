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
    import sys
    fileToChange = sys.argv[1]
    newDateTime = sys.argv[2]
    changeModificationDateTime(fileToChange, newDateTime)
