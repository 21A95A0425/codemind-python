z=int(input())
m=list(map(int,input().strip().split()))[:z]
a=[]
k=1
p=0
for i in range(len(m)):
    if i<z/2:
        a.append(m[z-k])
        k=k+1
    else:
        a.append(m[p])
        p=p+1
print(*a)