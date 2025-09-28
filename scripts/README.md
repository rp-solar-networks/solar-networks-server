# Scripts for Error Tracking

This directory contains utility scripts for managing and analyzing errors in the Solar Networks error tracking repository.

## Available Scripts

### error-stats.py

A Python script that generates statistics and reports about tracked errors.

**Prerequisites:**
- Python 3.6+
- GitHub CLI (`gh`) installed and authenticated

**Usage:**
```bash
# Generate text report
./scripts/error-stats.py

# Generate JSON output
./scripts/error-stats.py --format json

# Analyze trends for different time periods
./scripts/error-stats.py --days 7   # Last 7 days
./scripts/error-stats.py --days 90  # Last 90 days
```

**Features:**
- Total issue counts (open/closed)
- Breakdown by severity level
- Analysis by issue type
- Status distribution
- Trend analysis for recent issues
- Resolution rate calculation

**Example Output:**
```
============================================================
SOLAR NETWORKS ERROR TRACKING REPORT
============================================================
Generated: 2023-12-15 14:30:00

OVERVIEW
--------------------
Total Issues: 45
Open Issues: 12
Closed Issues: 33
Issues Created (Last 30 days): 8

BY SEVERITY
--------------------
High: 15 (33.3%)
Medium: 18 (40.0%)
Critical: 7 (15.6%)
Low: 5 (11.1%)

BY TYPE
--------------------
Bug: 28 (62.2%)
Performance: 8 (17.8%)
Security: 5 (11.1%)
Enhancement: 4 (8.9%)

Resolution Rate: 73.3%
============================================================
```

## Installation

1. Ensure Python 3.6+ is installed
2. Install GitHub CLI: https://cli.github.com/
3. Authenticate with GitHub: `gh auth login`
4. Make scripts executable: `chmod +x scripts/*.py`

## Contributing

To add new scripts:

1. Create your script in this directory
2. Add appropriate shebang line (`#!/usr/bin/env python3` for Python)
3. Make it executable with `chmod +x`
4. Add documentation to this README
5. Include usage examples and prerequisites

## Script Ideas

Future scripts that could be useful:

- **issue-template-validator**: Validate that issues follow the required templates
- **auto-triage**: Automatically add labels based on issue content
- **escalation-checker**: Identify issues that need escalation based on age/severity
- **metrics-dashboard**: Generate HTML dashboard with charts and graphs
- **notification-sender**: Send notifications for high-priority issues
- **duplicate-detector**: Find potential duplicate issues using text similarity