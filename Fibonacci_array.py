z=int(input())
m=list(map(int,input().split()))
a=m[0]
b=m[1]
f=True
for i in range(2,z):
    c=a+b
    a=b
    b=c
    if c!=m[i]:
        f=False
        break
if z>2 and f==True:
    print("yes")
else:
    print("no")
