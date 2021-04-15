Sql practice problems, with Postgres focus for now

##### Initialize
Perform once, at project inception
```bash
$ python sql/initializeBq.py
```

##### Repeatedly
If `raw` is the raw number:
```bash
$ python sandbox/obfuscate/*.py raw
```
After completing problem `sqlFile` with number `coded` and title `name`, update `sandbox/sqlMetadata.csv` then:
```bash
$ python sql/parseFiles.py
$ chmod 744 sql/*/coded-name.sql
```
If problem needs to be put back in order:
```bash
$ python sql/changeModTimeBack.py sql/*/coded-name.sql yyyy-mm-dd-hh:mm:ss
```

