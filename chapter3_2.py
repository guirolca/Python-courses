score = input("Enter Score: ")
try:
    sc=float(score)
except:
    sc=2
if sc >=0.9 :
    grade='A'
elif sc >=0.8 :
    grade='B'
elif sc >=0.7 :
    grade='C'
elif sc >=0.6 :
    grade='D'
else:
    grade='F'
if sc<=1:
    print(grade)
else:
    print('invalid score')
