import requests
import nmap
from colorama import Fore
from urllib.parse import urlparse
from utils import log_info

def detect_waf(url):
  """Detect WAF protection including Cloudflare."""
  try:
    response = requests.get(url)
    headers = response.headers
    
    waf_headers = [
      'x-waf', 'x-firewall', 'x-sucuri', 'x-sitelock',
      'x-distil', 'x-imperva', 'x-sophos', 'x-proxy', 'x-block'
    ]
    
    waf_detected = False
    cloudflare_detected = False
    
    # Check for common Cloudflare headers
    cloudflare_headers = [
      'cf-ray', 'cf-cache-status', 'cf-request-id'
    ]
    
    for header in cloudflare_headers:
      if header in headers:
        print(Fore.RED + f"Cloudflare detected: {header} = {headers[header]}")
        cloudflare_detected = True
    
    # Set WAF detection based on Cloudflare
    waf_detected = cloudflare_detected

    if not cloudflare_detected:
      print(Fore.GREEN + "No Cloudflare detected in headers.")
    
    # Check for other WAF indications
    for waf_header in waf_headers:
      if waf_header in headers:
        print(Fore.RED + f"WAF detected in headers: {waf_header} = {headers[waf_header]}")
        waf_detected = True
    
    if not waf_detected:
      print(Fore.GREEN + "No WAF detected in headers.")
    
  except requests.RequestException as e:
    print(Fore.RED + f"An error occurred during HTTP request: {e}")
  
  # Perform Nmap scan to further detect WAF on port 80 and 443
  if not cloudflare_detected:
    print(Fore.GREEN + "\nScanning with Nmap for additional WAF detection...")
    
    nm = nmap.PortScanner()
    target = urlparse(url).hostname
    ports = '80,443'
    
    try:
      nm.scan(hosts=target, arguments='--script http-waf-detect', ports=ports)
      
      # Output the results
      for host in nm.all_hosts():
        print(Fore.WHITE + f"\nHost: {host}")
        print(Fore.WHITE + "State:", nm[host].state())
        for protocol in nm[host].all_protocols():
          print(Fore.WHITE + f"\nProtocol: {protocol}")
          ports = nm[host][protocol].keys()
          for port in ports:
            print(Fore.GREEN + f"Port: {port}")
            if 'script' in nm[host][protocol][port]:
              print(Fore.RED + "Nmap WAF Detection Result:")
              print(Fore.RED + nm[host][protocol][port]['script'])
              waf_detected = True
            else:
              log_info("info", f"No WAF detected with Nmap on port {port}")
    
    except Exception as e:
      log_info("error", f"An error occurred during Nmap scan: {e}")
  return waf_detected