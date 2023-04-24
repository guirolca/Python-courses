import re
fname=input('Enter file name: ')
fh=open(fname)
count=0
for lines in fh:
    nums=re.findall('[0-9]+',lines)
    for num in nums:
        count=count+int(num)
print('Sum equals:',count)
