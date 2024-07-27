import argparse
from colorama import init, Fore
from utils.banner import print_banner
from utils.analysis import vulnerability_analysis
from utils.check_ips import check_ips
from utils.waf_detection import detect_waf
from utils.spider_urls import spider_urls
from utils.sql_detection import check_sql_injection

init()

def main(domain):
  print_banner()

  print(Fore.GREEN + "\n--- Detecting WAF ---")
  waf_detected = detect_waf(domain)
  
  print(Fore.GREEN + "\n--- Spidering URLs ---")
  urls = spider_urls(domain)
  
  ips_detected = False
  sql_injection_detected = False

  if urls:
    print(Fore.GREEN + "\n--- Checking IPS ---")
    ips_detected = check_ips(urls)
    
    print(Fore.GREEN + "\n--- Checking SQL Injection ---")
    sql_injection_detected = check_sql_injection(urls)
    
  else:
    print(Fore.RED + "No URLs found to check for vulnerabilities.")
  
  print(Fore.GREEN + "\n--- Vulnerability Analysis ---")
  vulnerability_analysis(waf_detected, ips_detected, sql_injection_detected, urls)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Web Vulnerability Scanner.')
  parser.add_argument('domain', type=str, help='The domain to scan for vulnerabilities.')
  args = parser.parse_args()
  
  main(args.domain)