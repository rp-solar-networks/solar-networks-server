#!/usr/bin/env python3
"""
Error Statistics Script for Solar Networks Error Tracking

This script provides statistics and insights about errors tracked in the repository.
Requires GitHub CLI (gh) to be installed and authenticated.
"""

import json
import subprocess
import sys
from collections import defaultdict, Counter
from datetime import datetime, timedelta
import argparse

def run_gh_command(cmd):
    """Run a GitHub CLI command and return the output."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {cmd}")
        print(f"Error: {e.stderr}")
        return None

def get_issues():
    """Fetch all issues from the repository."""
    cmd = "gh issue list --json number,title,labels,state,createdAt,updatedAt,assignees --limit 1000"
    output = run_gh_command(cmd)
    if output:
        return json.loads(output)
    return []

def analyze_by_severity(issues):
    """Analyze issues by severity level."""
    severity_counts = Counter()
    for issue in issues:
        labels = [label['name'] for label in issue['labels']]
        severity = 'unclassified'
        for label in labels:
            if 'critical' in label.lower():
                severity = 'critical'
                break
            elif 'high' in label.lower():
                severity = 'high'
                break
            elif 'medium' in label.lower():
                severity = 'medium'
                break
            elif 'low' in label.lower():
                severity = 'low'
                break
        severity_counts[severity] += 1
    return severity_counts

def analyze_by_type(issues):
    """Analyze issues by type."""
    type_counts = Counter()
    for issue in issues:
        labels = [label['name'] for label in issue['labels']]
        issue_type = 'other'
        for label in labels:
            if label.lower() in ['bug', 'performance', 'security', 'enhancement']:
                issue_type = label.lower()
                break
        type_counts[issue_type] += 1
    return type_counts

def analyze_by_status(issues):
    """Analyze issues by status."""
    status_counts = Counter()
    for issue in issues:
        labels = [label['name'] for label in issue['labels']]
        status = issue['state']  # open or closed
        for label in labels:
            if label.lower() in ['triage', 'in-progress', 'testing', 'resolved']:
                status = label.lower()
                break
        status_counts[status] += 1
    return status_counts

def analyze_trends(issues, days=30):
    """Analyze trends over the specified number of days."""
    cutoff_date = datetime.now() - timedelta(days=days)
    recent_issues = []
    
    for issue in issues:
        created_at = datetime.fromisoformat(issue['createdAt'].replace('Z', '+00:00'))
        if created_at.replace(tzinfo=None) > cutoff_date:
            recent_issues.append(issue)
    
    return len(recent_issues)

def generate_report(issues):
    """Generate a comprehensive error report."""
    total_issues = len(issues)
    open_issues = len([i for i in issues if i['state'] == 'open'])
    closed_issues = total_issues - open_issues
    
    severity_stats = analyze_by_severity(issues)
    type_stats = analyze_by_type(issues)
    status_stats = analyze_by_status(issues)
    recent_count = analyze_trends(issues, 30)
    
    print("=" * 60)
    print("SOLAR NETWORKS ERROR TRACKING REPORT")
    print("=" * 60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    print("OVERVIEW")
    print("-" * 20)
    print(f"Total Issues: {total_issues}")
    print(f"Open Issues: {open_issues}")
    print(f"Closed Issues: {closed_issues}")
    print(f"Issues Created (Last 30 days): {recent_count}")
    print()
    
    print("BY SEVERITY")
    print("-" * 20)
    for severity, count in severity_stats.most_common():
        percentage = (count / total_issues * 100) if total_issues > 0 else 0
        print(f"{severity.title()}: {count} ({percentage:.1f}%)")
    print()
    
    print("BY TYPE")
    print("-" * 20)
    for issue_type, count in type_stats.most_common():
        percentage = (count / total_issues * 100) if total_issues > 0 else 0
        print(f"{issue_type.title()}: {count} ({percentage:.1f}%)")
    print()
    
    print("BY STATUS")
    print("-" * 20)
    for status, count in status_stats.most_common():
        percentage = (count / total_issues * 100) if total_issues > 0 else 0
        print(f"{status.title()}: {count} ({percentage:.1f}%)")
    print()
    
    # Calculate resolution rate
    if closed_issues > 0:
        resolution_rate = (closed_issues / total_issues * 100)
        print(f"Resolution Rate: {resolution_rate:.1f}%")
    else:
        print("Resolution Rate: N/A (no closed issues)")
    
    print("=" * 60)

def main():
    parser = argparse.ArgumentParser(description="Generate error tracking statistics")
    parser.add_argument("--format", choices=['text', 'json'], default='text',
                       help="Output format (default: text)")
    parser.add_argument("--days", type=int, default=30,
                       help="Number of days for trend analysis (default: 30)")
    
    args = parser.parse_args()
    
    # Check if gh CLI is available
    if not run_gh_command("gh --version"):
        print("Error: GitHub CLI (gh) is not installed or not authenticated")
        print("Please install gh and run 'gh auth login' first")
        sys.exit(1)
    
    print("Fetching issues from repository...")
    issues = get_issues()
    
    if not issues:
        print("No issues found or error fetching issues")
        sys.exit(1)
    
    if args.format == 'json':
        # Output JSON format for programmatic use
        stats = {
            'total_issues': len(issues),
            'open_issues': len([i for i in issues if i['state'] == 'open']),
            'closed_issues': len([i for i in issues if i['state'] == 'closed']),
            'recent_issues': analyze_trends(issues, args.days),
            'by_severity': dict(analyze_by_severity(issues)),
            'by_type': dict(analyze_by_type(issues)),
            'by_status': dict(analyze_by_status(issues)),
            'generated_at': datetime.now().isoformat()
        }
        print(json.dumps(stats, indent=2))
    else:
        generate_report(issues)

if __name__ == "__main__":
    main()