a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in range(a):
    if i%2==0:
        c.append(b[i])
    else:
        d.append(b[i])
z=(sum(c)-sum(d))
if z%4==0:
    print("X")
else:
    print("Y")