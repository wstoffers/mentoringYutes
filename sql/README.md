Sql practice problems, with Postgres focus for now

### Initialize
Perform once, at project inception
```bash
$ python sql/initializeBq.py
```

### Repeatedly
If `raw` is the raw number:
```bash
$ python sandbox/obfuscate/*.py raw
```
Create file `sql/*/coded-name.sql` with number `coded` and title `name`. After completing problem, update `sandbox/sqlMetadata.csv` and then:
```bash
$ python sql/parseFiles.py
$ chmod 444 sql/*/coded-name.sql
```
If problem needs to be put back in order:
```bash
$ python sql/changeModTimeBack.py -f sql/*/coded-name.sql -t yyyy-mm-dd-hh:mm:ss
```

