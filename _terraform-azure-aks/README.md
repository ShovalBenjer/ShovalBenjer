# Terraform Azure AKS Module

![Terraform](https://img.shields.io/badge/Terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-%230072B6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-%23326CE5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)

[![Deployment Status](https://img.shields.io/badge/Deployed-Azure%20Cloud-blue?style=for-the-badge&logo=microsoftazure)](https://github.com/ShovalBenjer/terraform-azure-aks)

Opinionated Terraform module for provisioning and managing Azure Kubernetes Service (AKS) clusters with monitoring, networking, and security best practices built in.

## Features

- **AKS Cluster Provisioning** — Production-grade Kubernetes cluster on Azure with Log Analytics monitoring
- **Node Pool Management** — Configurable system and user node pools with auto-scaling, spot instances, and custom SKU sizing
- **Networking** — Azure CNI or kubenet plugin support, configurable pod and service CIDRs
- **Security** — Managed identities, Azure AD integration, custom CA trust, host encryption
- **Monitoring** — Integrated Azure Log Analytics with container insights
- **RBAC** — Role-based access control with Azure AD group binding

## Tech Stack

`Terraform` `Azure` `Azurerm Provider` `AKS` `Kubernetes` `HCL`

## Quick Start

```hcl
module "aks" {
  source  = "Azure/aks/azurerm"
  version = "10.1.1"

  resource_group_name = "my-rg"
  cluster_name        = "my-aks-cluster"
  location            = "eastus"
  kubernetes_version  = "1.29.4"
  dns_prefix          = "myaks"

  default_node_pool = {
    name       = "default"
    node_count = 3
    vm_size    = "Standard_DS2_v2"
  }
}
```

## Project Structure

```
.
├── README.md                          # This file
├── main.tf                            # Core AKS cluster resources
├── variables.tf                       # Module input variables
├── outputs.tf                         # Cluster outputs (kubeconfig, endpoint)
├── network.tf                         # VNet, subnet, and NSG configuration
├── nodepool.tf                        # Node pool definitions
└── monitoring.tf                      # Log Analytics workspace setup
```

## License

MIT