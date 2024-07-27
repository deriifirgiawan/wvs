from colorama import Fore

def vulnerability_analysis(waf_detected, ips_detected, sql_injection_detected, urls):
  vulnerability_score = 0
  
  if not waf_detected:
    vulnerability_score += 10

  if not ips_detected:
    vulnerability_score += 10

  if not sql_injection_detected:
    vulnerability_score += 20

  if urls:
    additional_score = min(len(urls), 100 - vulnerability_score)
    vulnerability_score += additional_score

  # Print results
  print(Fore.GREEN + "\nVulnerability Analysis:")
  print(Fore.YELLOW + f"WAF Detected: {Fore.GREEN + 'Yes' if waf_detected else Fore.RED + 'No'}")
  print(Fore.YELLOW + f"IPS Detected: {Fore.GREEN + 'Yes' if ips_detected else Fore.RED + 'No'}")
  print(Fore.YELLOW + f"SQL Injection Detected: {Fore.GREEN + 'Yes' if sql_injection_detected else Fore.RED + 'No'}")
  print(Fore.YELLOW + "URLs Found: " + Fore.GREEN + f"{len(urls)}")
  print(Fore.YELLOW + f"Estimated Vulnerability Score: {vulnerability_score}%")