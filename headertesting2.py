import json

fname=input('Enter the file name:')
fh=open(fname)
myjson=fh.read()
print(type(myjson))

i=0
def get_all(myjson, key):
while(i<1):
    if type(myjson) is str:
        myjson=myjson[0]
        print(type(myjson))
    if type(myjson) is dict:
        for jsonkey in myjson:
            if type(myjson[jsonkey]) in (list, dict):
                continue
            elif jsonkey == headers:
                print(myjson[jsonkey])
                i=1
    elif type(myjson) is list:
        print(a)
        for item in myjson:
            if type(item) in (list, dict):
                continue
