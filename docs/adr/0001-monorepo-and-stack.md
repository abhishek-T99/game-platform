# ADR 0001 — Monorepo and Phase 0 stack

## Status
Accepted

## Context
Solo developer, microservices learning project. Need low coordination
overhead, a fast local loop, and all-free/open-source tooling.

## Decision
- Monorepo (folder per service under /services).
- Local orchestration: docker-compose.
- Gateway: Nginx (static reverse-proxy config).
- Tracing: OpenTelemetry -> Grafana Tempo, viewed in Grafana OSS.
- Logging: structlog (JSON).
- Skeleton/template service: Django + DRF.
- Deps: uv. CI: GitHub Actions.

## Consequences
- Nginx routes are explicit (manual per service) — fine at this scale.
- Grafana+Tempo is slightly more setup than Jaeger's all-in-one, but keeps
  us in one observability ecosystem (metrics later land in the same Grafana).
- All tooling is self-hosted OSS; no paid tiers required.