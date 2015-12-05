__author__ = 'student'
from decimal import Decimal, getcontext
getcontext().prec = 2
S=float(input())
x=float(input())
y=int(input())
e=x/12
j=S
o=y
for g in range(round(x)+1,100):
    n=0
    S=j
    while n<y:
        S+=float(Decimal(str(x/100)))*S
        S-=float(Decimal(str((g/100)*j)))
        n+=1
    if n==y and S<=0.0:
        o=g
        b=((o/100)*j//0.01)/100
        print(b)
        break
