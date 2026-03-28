# 🌐 Wayback Spider

**A polite and easy-to-use web crawler that saves websites to the Internet Archive's Wayback Machine.**

Made for digital preservation — so we don't lose important parts of the web.

### Features
- Automatically follows internal links (same domain)
- Safe rate limiting with configurable delay
- Supports authenticated mode (higher limits + shows in your "My Web Archive")
- Logs all archived pages
- Beginner-friendly with good defaults

### Quick Start

### Installation

```bash
git clone https://github.com/jivsker/wayback-spider.git
cd wayback-spider

python -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
Authentication (Recommended)
Get your keys here: https://archive.org/account/s3.php
Bashexport SAVEPAGENOW_ACCESS_KEY="your_access_key"
export SAVEPAGENOW_SECRET_KEY="your_secret_key"
Usage
Bash# Safe basic usage
python wayback_spider.py https://example.com

# Recommended (with your account)
python wayback_spider.py https://example.com --authenticate --pages 15 --depth 2 --delay 35
Options

--pages 20 → archive up to 20 pages
--depth 2 → crawl 2 levels deep (recommended)
--delay 35 → wait 35 seconds between requests (be polite!)
--authenticate → use your account for better limits
--log → save list of URLs to archived_urls.log

Warning
Please be respectful of rate limits. Start small and don't crawl too aggressively.

Happy Archiving! 🕸️
