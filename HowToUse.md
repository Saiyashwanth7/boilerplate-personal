- use docker commands to start the pg,redis, rabbitmq (if needed) and other services along with their volume
- Docker commands:

```bash
docker-compose up -d

docker-compose ps
```

- Update the env details with the real details.
- CD to backend, run the docker commands, run this below command to start the backend:

```bash
uvicorn app.main:app --reload
```
