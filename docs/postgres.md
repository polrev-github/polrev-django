# Postgres

## Upgrade 13.5 to 15.10

### Spin up existing db container only

```bash
docker compose up db
```

### Dump to container

```bash
docker exec -t polrev-db-1 pg_dumpall -U polrev -f /tmp/db_dump.sql
```

### Copy to host

```bash
docker cp polrev-db-1:/tmp/db_dump.sql ./db_dump.sql
```

### Take container down
Ctrl-C

### Next steps
- Change docker-compose.yml to new postgres version
- Remove existing postgres container and volume

### Spin up new postgres container only

```bash
docker compose up db
```

### Copy dump into new container

```bash
docker cp db_dump.sql polrev-db-1:/tmp/db_dump.sql
```

### Restore to new container

```bash
docker exec -i polrev-db-1 psql -U polrev -f /tmp/db_dump.sql
```

### Test from web container
```bash
psql -h db -U polrev
```