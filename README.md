# 🌐 Wayback Spider

**A polite and easy-to-use web crawler that saves websites to the Internet Archive's Wayback Machine.**

Made for digital preservation — so we don't lose important parts of the web.

### Features
- Automatically follows internal links (same domain only)
- Safe rate limiting with configurable delay
- Authenticated mode (higher limits + shows in your "My Web Archive")
- Logs all successfully archived pages
- Beginner-friendly with good defaults

### Quick Start

#### 1. Installation

```bash
git clone https://github.com/jivsker/wayback-spider.git
cd wayback-spider

python -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
2. Authentication (Recommended)
Get your keys here: https://archive.org/account/s3.php
Then run:
Bashexport SAVEPAGENOW_ACCESS_KEY="your_access_key"
export SAVEPAGENOW_SECRET_KEY="your_secret_key"
3. Usage
Bash# Safe basic usage
python wayback_spider.py https://example.com

# Recommended command (with your account)
python wayback_spider.py https://example.com --authenticate --pages 15 --depth 2 --delay 35

# With logging
python wayback_spider.py https://example.com --authenticate --log
Options

--pages 15 → maximum pages to archive
--depth 2 → how deep to crawl (2 is recommended)
--delay 35 → seconds between requests (higher = safer)
--authenticate → use your account for better limits
--log → save list of archived URLs

Warning
Please start small and be respectful of rate limits. The Wayback Machine is a shared public service.

Happy Archiving! 🕸️
Made by jvskr
