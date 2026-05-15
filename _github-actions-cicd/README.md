# GitHub Actions CI/CD Pipelines

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-%232088FF.svg?style=for-the-badge&logo=github-actions&logoColor=white)
![Azure DevOps](https://img.shields.io/badge/Azure%20DevOps-%230078D7.svg?style=for-the-badge&logo=azure-devops&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI/CD-Automated-brightgreen?style=for-the-badge&logo=githubactions)

[![Build Status](https://img.shields.io/github/actions/workflow/status/ShovalBenjer/github-actions-cicd/ci.yml?branch=main&style=for-the-badge)](https://github.com/ShovalBenjer/github-actions-cicd/actions)

End-to-end CI/CD pipelines using GitHub Actions and Azure DevOps — automated builds, testing, container image publishing, and multi-environment deployments.

## Features

- **GitHub Actions Workflows** — Automated linting, testing, and deployment on push/PR
- **Azure DevOps Integration** — Classic and YAML pipelines for Azure-native deployments
- **Container CI** — Build and push Docker/OCI images to Azure Container Registry (ACR) and GitHub Container Registry (GHCR)
- **Multi-Environment Deployments** — Staging → Production promotion with manual approval gates
- **Infrastructure Validation** — Terraform plan/apply and Bicep build validation in CI
- **Code Quality** — Automated linting, type checks, and test coverage reporting

## Tech Stack

`GitHub Actions` `Azure DevOps` `YAML` `Docker` `Terraform` `Bicep` `Kubernetes`

## Pipeline Overview

```
┌─────────┐    ┌──────────┐    ┌──────────────┐    ┌──────────────┐
│   Push   │───▶│  Lint &  │───▶│   Build &    │───▶│  Deploy to   │
│ / PR     │    │  Test    │    │   Container  │    │  Staging     │
└─────────┘    └──────────┘    └──────────────┘    └──────┬───────┘
                                                          │
                                                    ┌─────▼──────┐
                                                    │  Manual    │
                                                    │  Approval  │
                                                    └─────┬──────┘
                                                          │
                                                    ┌─────▼──────┐
                                                    │  Deploy to │
                                                    │ Production │
                                                    └────────────┘
```

## Project Structure

```
.
├── README.md                          # This file
├── .github/
│   ├── workflows/
│   │   ├── ci.yml                     # Lint + test workflow
│   │   ├── build.yml                  # Container build workflow
│   │   ├── deploy-staging.yml         # Staging deployment
│   │   └── deploy-production.yml      # Production deployment with approval
│   └── actions/
│       └── setup-tools/               # Composite action for tool setup
├── azure-pipelines.yml                # Azure DevOps pipeline equivalent
├── Dockerfile                         # Multi-stage container build
└── scripts/
    ├── build.sh                       # Build script
    └── deploy.sh                      # Deployment script
```

## Getting Started

1. Clone the repository
2. Configure GitHub Secrets (`AZURE_CREDENTIALS`, `ACR_REGISTRY`, etc.)
3. Push to `main` to trigger the CI pipeline

## License

MIT