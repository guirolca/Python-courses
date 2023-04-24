fname=input('Enter file name: ')
fh=open(fname)
dic=dict()
for lines in fh:
    if not lines.startswith('From'):
        continue
    elif lines.startswith('From:'):
        continue
    words=lines.split()
    hourfull=words[5]
    hourparts=hourfull.split(':')
    hour=hourparts[0]
    dic[hour]=dic.get(hour,0)+1

hourlist=dic.items()
for k,v in sorted(hourlist):
    print(k,v)
