z=int(input())
m=list(map(int,input().strip().split()))
x,y=map(int,input().split())
a,b=min(x,y),max(x,y)
s=-1000
for i in m:
    if i<a or i>b:
        if i>s:
            s=i
if s==(-1000):
    print(-1)
else:
    print(s)