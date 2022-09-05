a=int(input())
b=[]
c=0
for i in range(1,a+1):
    c=i
    d=a%c
    if d==0:
        b.append(i)
d=len(b)
if d==2:
    print("prime")
else:
    print("not a prime")

