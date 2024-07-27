from urllib.parse import urlparse

def separate_urls(urls):
  urls_with_query = []
  urls_without_query = []

  for url in urls:
      parsed_url = urlparse(url)
      if parsed_url.query:
          urls_with_query.append(url)
      else:
          urls_without_query.append(url)
  
  return urls_with_query, urls_without_query