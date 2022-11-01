n=int(input())
m=list(map(int,input().strip().split()))[:n]
a,b=[],[]
s=0
f=False
for i in m:
    if i not in a:
        a.append(i)
    else:
        b.append(i)
for k in a:
    if k not in b:
        f=True
        if k>s:
            s=k
if f==True:
    print(s)
else:
    print(-1)