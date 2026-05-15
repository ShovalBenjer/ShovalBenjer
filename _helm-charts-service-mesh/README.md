# Helm Charts & Service Mesh

![Helm](https://img.shields.io/badge/Helm-%23277A9F.svg?style=for-the-badge&logo=helm&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-%23326CE5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Istio](https://img.shields.io/badge/Istio-%2306A5E9.svg?style=for-the-badge&logo=istio&logoColor=white)

[![Artifact Hub](https://img.shields.io/badge/Artifact%20Hub-Helm%20Charts-blue?style=for-the-badge&logo=artifacthub)](https://github.com/ShovalBenjer/helm-charts)

Production-ready Helm charts and Istio service mesh configurations for deploying microservices on Kubernetes clusters, with a focus on observability, traffic management, and security.

## Features

- **Modular Helm Charts** — Reusable chart templates with configurable values for common microservice patterns
- **Istio Service Mesh** — Traffic management, mTLS, circuit breaking, and observability
- **Monitoring Stack** — Prometheus, Grafana, and Jaeger dashboards pre-configured
- **Ingress Management** — Nginx and Istio Gateway configurations with TLS termination
- **GitOps Ready** — Designed for ArgoCD and Flux integration

## Tech Stack

`Helm` `Kubernetes` `Istio` `YAML` `Prometheus` `Grafana` `Go`

## Charts Available

| Chart | Description | Status |
|-------|-------------|--------|
| `api-gateway` | Istio-enabled API gateway with rate limiting | ✅ Stable |
| `auth-service` | OAuth2/OpenID Connect authentication microservice | ✅ Stable |
| `data-pipeline` | Event-driven data processing with Kafka consumer | ✅ Beta |
| `monitoring` | Prometheus + Grafana + Alertmanager stack | ✅ Stable |

## Quick Start

```bash
# Add the Helm repository
helm repo add shovalbenjer https://shovalbenjer.github.io/helm-charts

# Deploy a chart
helm install my-release shovalbenjer/api-gateway \
  --namespace production \
  --set ingress.host=api.example.com
```

## Istio Configuration

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: api-gateway
spec:
  hosts:
    - api.example.com
  http:
    - route:
        - destination:
            host: api-gateway
            port:
              number: 8080
      timeout: 30s
      retries:
        attempts: 3
        perTryTimeout: 10s
```

## Project Structure

```
.
├── README.md                          # This file
├── charts/
│   ├── api-gateway/
│   │   ├── Chart.yaml
│   │   ├── values.yaml
│   │   └── templates/
│   ├── auth-service/
│   │   ├── Chart.yaml
│   │   ├── values.yaml
│   │   └── templates/
│   ├── data-pipeline/
│   │   ├── Chart.yaml
│   │   ├── values.yaml
│   │   └── templates/
│   └── monitoring/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
├── istio/
│   ├── virtual-services/
│   ├── destination-rules/
│   ├── gateways/
│   └── authorization-policies/
└── scripts/
    └── deploy.sh                      # Helm install/upgrade script
```

## License

MIT