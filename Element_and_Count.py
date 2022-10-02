z=int(input())
m=list(map(int,input().strip().split()))[:z]
a=[]
s=0
m.sort
for i in range(z):
    if m[i] not in a:
        a.append(m[i])
for j in a:
    b=m.count(j)
    print(j,b,end=" ")