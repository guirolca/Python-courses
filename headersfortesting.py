import json

fname=input('Enter the file name:')
fh=open(fname)
data=fh.read()

try:
    js=json.loads(data)
except:
    js=None

for i in js:
    print(js['headers'])
