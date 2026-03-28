Markdown# 🌐 Wayback Spider

**A polite and easy-to-use web crawler that automatically archives websites to the Internet Archive's Wayback Machine.**

Perfect for digital preservation, lost media researchers, archivists, and anyone who wants to save websites before they disappear.

### Features
- Automatically follows internal links (stays on the same domain)
- Safe rate limiting with configurable delay
- Authenticated mode (higher limits + appears in your "My Web Archive")
- Built-in retry logic for common errors
- Logs archived URLs for easy tracking
- Works on **Windows, Linux, and macOS**

### Requirements
- Python 3.8 or higher
- An internet connection preferably wireless

### Installation

```bash
# Clone the repository
git clone https://github.com/jivsker/wayback-spider.git
cd wayback-spider

# Create virtual environment
python -m venv venv

# Activate the environment
# On Linux / macOS:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
Authentication (Recommended)
For higher rate limits and to have captures appear in your personal archive:

Go to https://archive.org/account/s3.php
Copy your Access Key and Secret Key

Then set them in your terminal:
Linux / macOS:
Bashexport SAVEPAGENOW_ACCESS_KEY="your_access_key_here"
export SAVEPAGENOW_SECRET_KEY="your_secret_key_here"
Windows:
PowerShellset SAVEPAGENOW_ACCESS_KEY=your_access_key_here
set SAVEPAGENOW_SECRET_KEY=your_secret_key_here
Usage Examples
Bash# Basic safe usage
python wayback_spider.py https://example.com

# Recommended (with your account)
python wayback_spider.py https://example.com --authenticate --pages 15 --depth 2 --delay 35

# Save a log of archived URLs
python wayback_spider.py https://example.com --authenticate --log
Command Line Options

OptionDefaultDescription--pages15Maximum number of pages to archive--depth2How deep to follow links (1 = only starting page)--delay35Seconds to wait between requests (higher = safer)--authenticateFalseUse your account (higher limits)--logFalseSave list of archived URLs to archived_urls.log
Important Notes

Start small — Use --pages 10 --depth 2 when testing.
The Wayback Machine has rate limits. Be respectful and don't crawl too aggressively.
Captures may take several hours to appear in "My Web Archive".
This is an early release (v1.0.0). Feedback and bug reports are welcome!


Happy Archiving! 🕸️
Made by jivsker
