text = "X-DSPAM-Confidence:    0.8475"
pos=text.find(':')
snum=text[pos+1:]
snum2=snum.lstrip()
print(float(snum2))
