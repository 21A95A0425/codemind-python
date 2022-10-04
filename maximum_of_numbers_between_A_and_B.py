z=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
c=[]
for i in range(z):
    if a<=m[i]<=b:
        c.append(m[i])
        s=1
if s==1:
    print(max(c))
else:
    print(-1)
