#!/usr/bin/env python3
"""
Profile Health Monitor - Comprehensive GitHub profile health checker
Runs: broken links, badge uptime, SEO analysis, keyword density
"""

import re
import sys
import json
import argparse
from datetime import datetime
from typing import List, Dict, Set, Tuple
from pathlib import Path

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


class ProfileHealthMonitor:
    ALLOWED_DOMAINS = {
        'github.com', 'githubusercontent.com', 'shovalbenjer.github.io',
        'ghchart.rshah.org', 'github-readme-stats.vercel.app',
        'admaven-demo.fly.dev', 'fly.dev',
        'linkedin.com',
        'img.shields.io', 'gist.githubusercontent.com',
        'vercel.app',
    }

    NON_CRITICAL_DOMAINS = {'linkedin.com', 'vercel.app'}

    REQUIRED_KEYWORDS = [
        'DevOps', 'IaC', 'Azure', 'Data Engineering',
        'Python', 'AI', 'ML', 'AWS', 'Kubernetes'
    ]

    REQUIRED_SECTIONS = [
        'Who I am', 'Tech Stack', 'Engineering', 'Financial',
        'Demos', 'Live Demo', 'GitHub Stats'
    ]

    def __init__(self, readme_path: str = 'README.md', use_network: bool = True):
        self.readme_path = Path(readme_path)
        self.use_network = use_network and REQUESTS_AVAILABLE
        self.results = {
            'timestamp': datetime.utcnow().isoformat(),
            'readme': self.readme_path.name,
            'checks': {},
            'broken_links': [],
            'failed_badges': [],
            'seo_issues': [],
            'warnings': [],
            'pass': True
        }

    def load_readme(self) -> str:
        """Load README content"""
        if not self.readme_path.exists():
            raise FileNotFoundError(f"README not found at {self.readme_path}")
        return self.readme_path.read_text()

    def extract_urls(self, content: str) -> Set[str]:
        """Extract all URLs from README"""
        patterns = [
            r'\[([^\]]+)\]\(([^)]+)\)',
            r'src=["\']([^"\']+)["\']',
            r'href=["\']([^"\']+)["\']',
        ]
        urls = set()
        for pattern in patterns:
            for match in re.finditer(pattern, content):
                url = match.group(1)
                urls.add(url)
        return urls

    def check_broken_links(self, content: str) -> Tuple[List[str], List[str]]:
        """Check all external links for accessibility"""
        if not self.use_network:
            return [], ["Network checks disabled - install requests library"]

        broken = []
        warnings = []
        urls = self.extract_urls(content)

        for url in sorted(urls):
            try:
                parsed = requests.utils.urlparse(url)
                if not parsed.scheme or parsed.scheme not in ('http', 'https'):
                    continue

                domain = parsed.netloc.lower()

                if not any(domain.endswith(d) or d in domain.split('.')
                           for d in self.ALLOWED_DOMAINS):
                    warnings.append(f"External domain not in allowlist: {url}")
                    continue

                timeout = 10 if any(d in domain for d in self.NON_CRITICAL_DOMAINS) else 5
                response = requests.head(url, timeout=timeout, allow_redirects=True)

                if response.status_code >= 400:
                    broken.append(f"HTTP {response.status_code}: {url}")
                elif response.status_code < 200:
                    broken.append(f"Invalid response: {url}")

            except requests.exceptions.Timeout:
                if any(d in url for d in self.NON_CRITICAL_DOMAINS):
                    warnings.append(f"Timeout (may be rate-limited): {url}")
                else:
                    broken.append(f"Timeout: {url}")
            except Exception as e:
                broken.append(f"Error: {url} - {str(e)}")

        return broken, warnings

    def check_badges(self, content: str) -> Tuple[List[str], List[str]]:
        """Check badge image accessibility"""
        if not self.use_network:
            return [], ["Network checks disabled"]

        badge_patterns = [
            r'https://img\.shields\.io/badge/[^\s\)]+',
            r'https://ghchart\.rshah\.org/[^\s\)]+',
            r'https://github-readme-stats\.vercel\.app/api[^\s\)]+',
            r'https://github-readme-stats\.vercel\.app/api/top-langs/[^\s\)]+',
        ]

        badge_urls = set()
        for pattern in badge_patterns:
            badge_urls.update(re.findall(pattern, content))

        failed = []
        slow = []

        for badge_url in badge_urls:
            try:
                response = requests.head(badge_url, timeout=8, allow_redirects=True)
                if response.status_code >= 400:
                    failed.append(f"HTTP {response.status_code}: {badge_url[:60]}")
                else:
                    print(f"  ✅ {badge_url[:60]}...")
            except requests.exceptions.Timeout:
                slow.append(badge_url[:60])
            except Exception as e:
                failed.append(f"Error: {e} - {badge_url[:60]}")

        if slow:
            print(f"\n⚠️  Slow badges ({len(slow)}):")
            for b in slow[:3]:
                print(f"  ⏱️  {b}")

        return failed, slow

    def check_seo(self, content: str) -> Tuple[List[str], List[str]]:
        """Check SEO and discoverability"""
        issues = []
        warnings = []

        content_lower = content.lower()

        print("📊 SEO Keyword Analysis:")
        for keyword in self.REQUIRED_KEYWORDS:
            if keyword.lower() in content_lower:
                print(f"  ✅ Found: {keyword}")
            else:
                issues.append(f"Missing core keyword: {keyword}")

        print("\n🔍 Code Quality Check:")
        issue_markers = ['TODO', 'FIXME', 'HACK', 'XXX', 'BUG']
        for marker in issue_markers:
            matches = re.findall(r'.{0,20}' + re.escape(marker) + r'.{0,20}', content, re.IGNORECASE)
            if matches:
                for m in matches:
                    warnings.append(f"Found '{marker}': {m.strip()}")

        print("\n📋 Structure Validation:")
        for section in self.REQUIRED_SECTIONS:
            if section in content:
                print(f"  ✅ Section: {section}")
            else:
                warnings.append(f"Missing section: {section}")

        # Check for proper heading hierarchy
        heading_pattern = r'^#{1,6} '
        if content.count('# ') < 2:
            warnings.append("README should have at least one main heading (#)")

        # Check for image alt text
        images = re.findall(r'!\[([^\]]*)\]\([^)]+\)', content)
        missing_alt = [img for img in images if not img.strip()]
        if missing_alt:
            warnings.append(f"{len(missing_alt)} images missing alt text")

        return issues, warnings

    def run_all_checks(self):
        """Execute all health checks"""
        print("🏥 Profile Health Monitor\n" + "="*60)

        try:
            content = self.load_readme()
        except FileNotFoundError as e:
            print(f"❌ {e}")
            self.results['pass'] = False
            return self.results

        print(f"📄 README: {self.readme_path} ({len(content)} chars)\n")

        # 1. Broken links
        print("\n🔗 Broken Link Check:")
        broken, warnings = self.check_broken_links(content)
        self.results['broken_links'] = broken
        self.results['warnings'].extend(warnings)
        if broken:
            print(f"❌ {len(broken)} broken link(s):")
            for b in broken[:5]:
                print(f"  • {b}")
        else:
            print("✅ All external links are healthy!")

        # 2. Badge uptime
        print("\n🏷️  Badge Uptime Check:")
        badge_failures, slow_badges = self.check_badges(content)
        self.results['failed_badges'] = badge_failures
        if badge_failures:
            print(f"❌ {len(badge_failures)} failed badge(s):")
            for b in badge_failures[:5]:
                print(f"  • {b}")
        else:
            print("✅ All badges are accessible!")

        # 3. SEO & structure
        print("\n🔎 SEO & Discoverability Check:")
        seo_issues, seo_warnings = self.check_seo(content)
        self.results['seo_issues'] = seo_issues
        self.results['warnings'].extend(seo_warnings)
        if seo_issues:
            for issue in seo_issues:
                print(f"  ❌ {issue}")
        else:
            print("✅ SEO check passed!")

        print("\n" + "="*60)
        total_errors = len(broken) + len(badge_failures) + len(seo_issues)
        if total_errors > 0:
            print(f"❌ Profile Health: {total_errors} issue(s) found")
            self.results['pass'] = False
            sys.exit(1)
        else:
            print("✅ Profile Health: All checks passed!")
            self.results['pass'] = True

        return self.results


def main():
    parser = argparse.ArgumentParser(description='Profile Health Monitor')
    parser.add_argument('--readme', default='README.md', help='Path to README file')
    parser.add_argument('--offline', action='store_true', help='Skip network checks')
    parser.add_argument('--json', action='store_true', help='Output results as JSON')
    parser.add_argument('--check-seo', action='store_true', help='Run SEO check only')
    parser.add_argument('--check-links', action='store_true', help='Run link check only')
    parser.add_argument('--check-badges', action='store_true', help='Run badge check only')
    args = parser.parse_args()

    monitor = ProfileHealthMonitor(
        readme_path=args.readme,
        use_network=not args.offline
    )

    if args.json:
        results = monitor.run_all_checks()
        print(json.dumps(results, indent=2))
    elif args.check_seo:
        content = monitor.load_readme()
        issues, warnings = monitor.check_seo(content)
        sys.exit(1 if issues else 0)
    elif args.check_links:
        content = monitor.load_readme()
        broken, warnings = monitor.check_broken_links(content)
        sys.exit(1 if broken else 0)
    elif args.check_badges:
        content = monitor.load_readme()
        failed, slow = monitor.check_badges(content)
        sys.exit(1 if failed else 0)
    else:
        monitor.run_all_checks()


if __name__ == '__main__':
    main()
