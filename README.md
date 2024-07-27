# Web Vulnerability Scanner (WVS)

## Description

The Web Vulnerability Scanner (WVS) is a tool designed to detect vulnerabilities on websites. This tool checks for the presence of Web Application Firewalls (WAF), Intrusion Prevention Systems (IPS), and potential SQL Injection vulnerabilities. WVS employs various detection and analysis methods to provide a comprehensive assessment of a website's security.

## Features

- **WAF Detection:** Detects WAF presence using HTTP headers and performs additional security checks with Nmap.
- **URL Spidering:** Extracts URLs from the given webpage for further analysis.
- **IPS Detection:** Checks for the presence of IPS by comparing response times and status codes.
- **SQL Injection Testing:** Identifies potential SQL Injection vulnerabilities using various payloads and examines server responses.

## Installation

1. **Clone Repository:**

```bash
  git clone https://github.com/deriifirgiawan/wvs.git
```

2. **Install Dependencies:**

```bash
  pip install -r requirements.txt
```

## Usage

```bash
  python wvs.py https://example.com
```

## Example Output

```txt
--- Detecting WAF ---
Cloudflare detected: cf-ray = 8a9348b82be1be6a-CGK
No WAF detected in headers.

--- Spidering URLs ---
+----------------------------------------------+
| URL                                          |
+----------------------------------------------+
| https://example.com/page1                   |
| https://example.com/page2                   |
+----------------------------------------------+

--- Checking IPS ---
Different status codes detected, potential IPS present.

--- Vulnerability Analysis ---
WAF Detected: No
IPS Detected: Yes
URLs Found: 2
Estimated Vulnerability Score: 60%
```

## Contact

- Author: deriifirgiawan
- Email: derifirgiawan025@gmail.com
