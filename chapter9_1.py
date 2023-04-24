fname=input('Enter the file name:')
fh=open(fname)
emails=dict()
for line in fh :
    if not line.startswith('From'):
        continue
    elif line.startswith('From:'):
        continue
    words=line.split()
    name=words[1]
    emails[name]=emails.get(name,0)+1

namemax=None
nummax=None
for k,v in emails.items():
    if nummax==None or v>nummax:
        nummax=v
        namemax=k
print(namemax,nummax)
