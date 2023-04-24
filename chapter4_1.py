def computepay(h,r):
    if h<=40:
        pay=h*r
    else:
        pay=40*r+(h-40)*(1.5*r)
    return pay

hrs = input('Enter Hours:')
ihrs=float(hrs)
rate=input('Enter rate:')
irate=float(rate)
p = computepay(ihrs,irate)
print(p)
