from colorama import Fore

def log_info(type, messages):
  typeText = "INFO"
  colorText = Fore.GREEN
  if type == "info":
    typeText = "INFO"
    colorText = Fore.GREEN
  elif type == 'success':
    typeText = "SUCCESS"
    colorText = Fore.GREEN
  elif type == "warning":
    colorText = Fore.YELLOW
    typeText = "WARNING"
  else:
    colorText = Fore.RED
    typeText = "ERROR"
  print(Fore.WHITE + "[" + colorText + typeText + Fore.WHITE + "]" + " " + messages)