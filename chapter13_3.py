import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address=input('Enter location:')
    if len(address)<1:
        continue
    print('Retrieving',address)

    uh=urllib.request.urlopen(address,context=ctx)
    data=uh.read().decode()
    try:
        js=json.loads(data)
    except:
        js=None

    count=0
    sum=0
    for item in js['comments']:
        count=count+1
        sum=sum+int(item['count'])

    print('Count', count)
    print('Sum', sum)
