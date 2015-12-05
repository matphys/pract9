def f(y,z):
    return 108-((815-(1500/z))/y)
x=4.0
for n in range(1,31):
    e=x
    x=f(e,x)
    if n==29:
        print(f(e,x))
x=4.50
e=4.25
g=1
h=1
while f(e,x)-f(g,h)!=0.0:
    g=e
    h=x
    e=x
    x=f(e,x)
print(x)
