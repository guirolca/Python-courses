fname = input("Enter file name: ")
fh = open(fname)
count=0
sum=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    posline=line.find(':')
    snum=line[posline+1:]
    snum2=float(snum.lstrip())
    total=total+snum2
average=sum/count
print('Average spam confidence: ',average)
