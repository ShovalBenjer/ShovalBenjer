## Overview

Adds comprehensive automated health monitoring for the GitHub profile README and deployed demos.

## Components

- **README Lint** — runs on every push to `main` that modifies `README.md`
- **Broken Link Checker** — daily at 09:00 UTC, validates all external links  
- **Badge Uptime Monitor** — daily at 09:00 UTC, ensures shields.io and GitHub Stats are live
- **Deployed Demo Health** — daily at 09:00 UTC, pings AdMaven ETL Dashboard
- **SEO & Discoverability** — daily at 09:00 UTC, validates keywords and structure

All checks run simultaneously; a failure triggers an automatic GitHub Issue labeled `profile-health`, `automation`, `monitoring`.

## Local Testing

```bash
cd scripts
pip install -r requirements.txt
python profile-health-monitor.py
```

## Documentation
See `.github/PROFILE_MONITORING.md` for full details.
