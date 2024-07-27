import requests
from tabulate import tabulate
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from utils import log_info

def spider_urls(url):
  """Extract all URLs from the given webpage."""
  try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = set()

    # Extract URLs from anchor tags
    links = soup.find_all('a', href=True)
    for link in links:
      href = link['href']
      full_url = urljoin(url, href)
      urls.add(full_url)

    # Extract URLs from script tags
    scripts = soup.find_all('script', src=True)
    for script in scripts:
      src = script['src']
      full_url = urljoin(url, src)
      urls.add(full_url)

    # Extract URLs from iframe tags
    iframes = soup.find_all('iframe', src=True)
    for iframe in iframes:
      src = iframe['src']
      full_url = urljoin(url, src)
      urls.add(full_url)
    
    tmpUrl = list(urls)
    converted_url = [[item] for item in tmpUrl]
    print(tabulate(converted_url, headers=['URL'], tablefmt='grid'))

    return list(urls)    
  except requests.RequestException as e:
    log_info('error', f"An error occurred: {e}")
    return []