z=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
s=0
b=[]
for i in a:
    if i<x or i>y:
        b.append(i)
#print(sum(b))
        s=1
if s==0:
    print(-1)
else:
    print(min(b))
