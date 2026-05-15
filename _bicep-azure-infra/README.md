# Bicep Azure Infrastructure Templates

![Bicep](https://img.shields.io/badge/Bicep-%230E8098.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-%230072B6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![IaC](https://img.shields.io/badge/IaC-Infrastructure%20as%20Code-informational?style=for-the-badge&logo=terraform)

[![Deployment Status](https://img.shields.io/badge/Deployed-Azure%20Cloud-blue?style=for-the-badge&logo=microsoftazure)](https://github.com/ShovalBenjer/bicep-azure-infra)

Reusable Bicep modules and templates for deploying Azure infrastructure — resource groups, storage accounts, container apps, function apps, and Kubernetes clusters.

## Features

- **Modular Architecture** — Reusable Bicep modules for common Azure resources
- **Container Apps** — Azure Container Apps with managed identities and Dapr integration
- **Function Apps** — Containerized Azure Functions with custom domains and SSL
- **Storage & Networking** — Storage accounts, VNets, private endpoints, and DNS zones
- **Kubernetes** — AKS cluster templates with node pool and addon configuration
- **Parameterized Deployments** — CI/CD-ready with environment-specific parameter files

## Tech Stack

`Bicep` `Azure` `IaC` `ARM Templates` `Azure CLI` `PowerShell`

## Quick Start

Deploy a resource group with storage and networking:

```bash
az deployment sub create \
  --location eastus \
  --template-file main.bicep \
  --parameters \
    resourceGroupName='my-rg' \
    location='eastus' \
    storageAccountName='mystorage${uniqueString}'
```

## Project Structure

```
.
├── README.md                          # This file
├── main.bicep                         # Main entry template
├── modules/
│   ├── storage/
│   │   ├── main.bicep                 # Storage account module
│   │   └── outputs.bicep
│   ├── networking/
│   │   ├── vnet.bicep                 # Virtual network module
│   │   └── private-endpoint.bicep
│   ├── container-app/
│   │   └── main.bicep                 # Container App module
│   └── kubernetes/
│       └── aks.bicep                  # AKS cluster module
├── parameters/
│   ├── dev.parameters.json
│   ├── staging.parameters.json
│   └── prod.parameters.json
└── scripts/
    └── deploy.sh                      # CI/CD deployment script
```

## License

MIT