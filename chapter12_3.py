import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count= input('Enter count: ')
pos= input('Enter position: ')
i=1
urls=list()
print('Retrieving: ',url)

while i<=int(count):
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')

  # Retrieve all of the anchor tags
  tags = soup('a')

  for tag in tags:
      urlonly=tag.get('href', None)
      urls.append(urlonly)
  url=urls[int(pos)-1]
  print('Retrieving: ',url)

  i=i+1
  urls=list()
