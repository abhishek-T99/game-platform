# game-platform

A containerised game platform built with Django REST Framework, backed by PostgreSQL and RabbitMQ, with distributed tracing via OpenTelemetry + Tempo and dashboards in Grafana.

## Services

| Service    | Description                        | Local URL                                      |
|------------|------------------------------------|------------------------------------------------|
| hello      | Django REST API                    | https://game-platform.local/hello/             |
| nginx      | Reverse proxy / TLS termination    | https://game-platform.local                    |
| postgres   | Primary database                   | localhost:5432                                 |
| rabbitmq   | Message broker                     | localhost:5672 · UI: http://localhost:15672     |
| tempo      | Distributed tracing backend        | localhost:3200                                 |
| grafana    | Observability dashboards           | http://localhost:3000 (admin / admin)          |

## Prerequisites

- Docker Desktop
- [mkcert](https://github.com/FiloSottile/mkcert) for local HTTPS

## First-time setup

```bash
# 1. Trust the local CA (once per machine)
mkcert -install

# 2. Generate the TLS certificate
cd infra/nginx/certs
mkcert game-platform.local

# 3. Add the domain to your hosts file (run as Administrator on Windows)
echo "127.0.0.1 game-platform.local" >> C:\Windows\System32\drivers\etc\hosts
```

## Running

```bash
docker compose up --build
```

## Running tests

```bash
cd services/hello
pytest
```
