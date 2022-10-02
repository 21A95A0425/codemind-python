z=int(input())
m=list(map(int,input().strip().split()))
x,y=map(int,input().split())
a,b=min(x,y),max(x,y)
s=0
for i in m:
    if i<a or i>b:
        s+=i
print(s)