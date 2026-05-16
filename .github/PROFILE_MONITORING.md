# Profile Health Monitoring

Automated health checks for the GitHub profile to ensure optimal performance, accessibility, and discoverability.

## Overview

This system runs continuous checks on the profile README and all deployed demos, providing early warnings for issues through GitHub Issues.

## Checks

### 1. README Linting (`readme-lint`)
- **When:** On every push to `main` that modifies `README.md`
- **Tool:** [markdownlint](https://github.com/DavidAnson/markdownlint)
- **Purpose:** Enforces consistent markdown style and catches syntax issues

### 2. Broken Link Checker (`broken-links`)
- **When:** Daily at 9:00 AM UTC
- **Scope:** All external links in README (GitHub, Shields.io, deployed demos, etc.)
- **Tool:** Custom Python script using `requests`
- **Purpose:** Detects 404s, timeouts, and broken references

### 3. Badge Uptime Monitor (`badge-uptime`)
- **When:** Daily at 9:00 AM UTC
- **Scope:** Static badge images (Shields.io, GitHub Readme Stats, GHChart)
- **Purpose:** Ensures all dynamic badges remain accessible

### 4. Deployed Demo Health (`demo-uptime`)
- **When:** Daily at 9:00 AM UTC
- **Scope:** Live deployed applications (AdMaven ETL Dashboard)
- **Purpose:** Verifies deployed applications are online and responding

### 5. SEO & Discoverability (`seo-check`)
- **When:** Daily at 9:00 AM UTC
- **Checks:**
  - Core keyword presence (DevOps, IaC, Azure, Data Engineering, Python, AI, ML)
  - Required section headings
  - Missing alt text on images
  - Code quality markers (TODO, FIXME, HACK)

## Alerting

When any check fails, the workflow automatically:
1. Creates a GitHub Issue titled `🚨 Profile Health Alert - [date]`
2. Labels it with `profile-health`, `automation`, `monitoring`
3. Includes which specific jobs failed and links to the workflow run

## Manual Execution

Run specific checks manually via workflow dispatch:

```bash
# All checks
gh workflow run profile-health.yml

# Specific check only
gh workflow run profile-health.yml -f check-type=links
gh workflow run profile-health.yml -f check-type=badges
gh workflow run profile-health.yml -f check-type=seo
gh workflow run profile-health.yml -f check-type=lint
```

## Local Testing

Run checks locally using the monitoring script:

```bash
# Install dependencies
cd scripts
pip install -r requirements.txt

# Run all checks
python profile-health-monitor.py

# Run specific check only
python profile-health-monitor.py --check-links
python profile-health-monitor.py --check-badges
python profile-health-monitor.py --check-seo
```

## Schedule

| Check | Frequency | Time (UTC) |
|-------|-----------|------------|
| Lint | On push | Event-driven |
| Links | Daily | 09:00 |
| Badges | Daily | 09:00 |
| Demos | Daily | 09:00 |
| SEO | Daily | 09:00 |

## Badge Uptime Monitoring

Badge uptime checks verify that dynamic badges from services like Shields.io, GitHub Readme Stats, and GHChart render correctly. Failed badges appear as broken images on the profile.

### Badge Sources Monitored
- `img.shields.io` - Static and dynamic badges
- `ghchart.rshah.org` - Contribution chart badges  
- `github-readme-stats.vercel.app` - GitHub stats and top languages
