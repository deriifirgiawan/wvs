import pyfiglet
from colorama import Fore

BOLD = '\033[1m'
RESET = '\033[0m'
def print_banner():
  print("\n")
  font = pyfiglet.Figlet(font='colossal')
  banner = font.renderText("WVS")
  print(Fore.GREEN + banner)
  print("<=====================================================================>")
  print(Fore.GREEN + f" {BOLD}- Tools Name: Web Vulnerability Scanner{RESET}")
  print(Fore.GREEN + f" {BOLD}- Author: deriifirgiawan{RESET}")
  print(Fore.GREEN + f" {BOLD}- Github: https://github.com/deriifirgiawan/wvs{RESET}")
  print(Fore.GREEN + "<=====================================================================>")
  print("\n")
  print(Fore.YELLOW + f"{BOLD}WARNING: This tool is intended for educational and informational purposes only. {RESET}")
  print(Fore.YELLOW + f"{BOLD}Do not use it on systems or websites that you do not own or have explicit permission to test. {RESET}")
  print(Fore.YELLOW + f"{BOLD}Improper use of this tool can lead to legal consequences. Always follow ethical hacking practices and local laws.{RESET}")
  print("\n")