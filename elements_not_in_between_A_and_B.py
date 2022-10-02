z=int(input())
m=list(map(int,input().strip().split()))
x,y=map(int,input().split())
a,b=min(x,y),max(x,y)
k=[]
for i in range(len(m)):
    if m[i]<a or m[i]>b:
        k.append(m[i])
if len(k)==0:
    print(-1)
else:
    print(*k)