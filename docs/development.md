# Development

## Setup

```bash
cp .env.dev.example .env
cp docker-compose.dev.yml docker-compose.override.yml
docker compose up
```

### Problem
The Django container will fail initially because Minio needs to be configured.

You need to login to minio and create buckets.

### Minio

http://s3.docker.localhost:9000/

login credentials

    minio-access-key

    minio-secret-key

create polrev and polrev-backup buckets

### Solutions?
https://stackoverflow.com/questions/66412289/minio-add-a-public-bucket-with-docker-compose
