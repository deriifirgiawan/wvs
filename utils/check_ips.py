import requests
import time
from colorama import Fore
from utils import separate_urls, log_info

def check_ips(urls):
  """Check for potential IPS presence using timing and response code comparison."""
  urls_with_query, _ = separate_urls(urls=urls)

  if not urls_with_query:
    print(Fore.RED + "No URLs with query parameters found to check for IPS.")
    return False
  
  ips_detected = False

  # List of payloads to test IPS
  payloads = [
    "' OR '1'='1",
    "' OR '1'='1' --",
    "' OR 1=1 --",
    "' OR 'a'='a",
    "' OR 'a'='a' --"
  ]

  for url_params in urls_with_query:
    for payload in payloads:
      try:
        if '=' in url_params:
          base_url, param = url_params.split('=', 1)
          malicious_payload = base_url + '=' + param + payload
        else:
          malicious_payload = url_params + payload
        
        # Measure response time for normal payload
        start_time = time.time()
        normal_response = requests.get(url_params)
        normal_time = time.time() - start_time
        
        # Measure response time for malicious payload
        start_time = time.time()
        malicious_response = requests.get(malicious_payload)
        malicious_time = time.time() - start_time
        
        # Compare response times and status codes
        if normal_response.status_code != malicious_response.status_code:
          log_info("info", f"Different status codes detected with payload '{payload}', potential IPS present.")
          ips_detected = True
          break  # Exit loop if IPS is detected
        elif malicious_time > normal_time * 1.5:
          log_info('info', f"Significant delay detected with payload '{payload}', potential IPS present.")
          ips_detected = True
          break  # Exit loop if IPS is detected
        else:
          log_info('success', f"No significant difference detected with payload '{payload}', IPS presence is uncertain.")
      except requests.RequestException as e:
        print(Fore.RED + f"An error occurred: {e}")
    
    if ips_detected:
      break  # Exit outer loop if IPS is detected
  
  return ips_detected