#!/usr/bin/env python3
"""
🌐 Wayback Spider
A polite crawler that archives websites to the Internet Archive's Wayback Machine.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import argparse
import sys
from collections import deque

try:
    import savepagenow
except ImportError:
    print("❌ 'savepagenow' is not installed. Run: pip install -r requirements.txt")
    sys.exit(1)

def normalize_url(url):
    return url.rstrip('/')

def is_same_domain(url, base_domain):
    parsed = urlparse(url)
    return parsed.netloc == base_domain or parsed.netloc.endswith('.' + base_domain)

def get_links(url, base_domain):
    try:
        headers = {'User-Agent': 'WaybackSpider - Polite personal archiver (github.com/jivsker)'}
        r = requests.get(url, headers=headers, timeout=15)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'lxml')
        
        links = set()
        for a in soup.find_all('a', href=True):
            full_url = urljoin(url, a['href'])
            if full_url.startswith(('http://', 'https://')):
                if not any(full_url.startswith(x) for x in ['mailto:', 'tel:', 'javascript:', '#']):
                    if is_same_domain(full_url, base_domain):
                        links.add(normalize_url(full_url))
        return links
    except Exception:
        return set()

def archive_url(url, authenticate=False):
    print(f"📤 Archiving → {url}")
    try:
        archived_url, was_fresh = savepagenow.capture_or_cache(url, authenticate=authenticate)
        status = "✅ Fresh capture!" if was_fresh else "📦 Already archived"
        print(f"   {status}")
        return True
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="🌐 Wayback Spider - Polite Web Archiver")
    parser.add_argument("url", nargs="?", help="Starting URL (e.g. https://example.com)")
    parser.add_argument("--pages", type=int, default=15, help="Max pages to archive (default: 15)")
    parser.add_argument("--depth", type=int, default=2, help="Max crawl depth (default: 2)")
    parser.add_argument("--delay", type=int, default=35, help="Delay in seconds between requests")
    parser.add_argument("-a", "--authenticate", action="store_true", help="Use authenticated mode (recommended)")
    parser.add_argument("--log", action="store_true", help="Save archived URLs to archived_urls.log")

    args = parser.parse_args()

    if not args.url:
        parser.print_help()
        sys.exit(1)

    base_domain = urlparse(args.url).netloc
    print(f"🚀 Starting Wayback Spider for {base_domain}")
    print(f"   Max pages : {args.pages} | Depth : {args.depth} | Delay : {args.delay}s\n")

    queue = deque([(args.url, 0)])
    visited = set()
    archived_count = 0

    log_file = open("archived_urls.log", "a", encoding="utf-8") if args.log else None

    while queue and archived_count < args.pages:
        url, depth = queue.popleft()
        url = normalize_url(url)

        if url in visited or depth > args.depth:
            continue

        visited.add(url)

        # Archive the page
        if archive_url(url, authenticate=args.authenticate):
            archived_count += 1
            if log_file:
                log_file.write(f"{url}\n")

        # Discover new links
        if depth < args.depth and archived_count < args.pages:
            new_links = get_links(url, base_domain)
            for link in new_links:
                if link not in visited:
                    queue.append((link, depth + 1))

        # Be polite
        if archived_count < args.pages and queue:
            time.sleep(args.delay)

    if log_file:
        log_file.close()

    print(f"\n🎉 Finished! Archived {archived_count} pages from {base_domain}")
    print(f"   Check your archives later at: https://web.archive.org/web/*/{base_domain}/*")

if __name__ == "__main__":
    main()
