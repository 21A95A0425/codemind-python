z=int(input())
m=list(map(int,input().split()))
a=[]
b=[]
c=[]
for i in range(len(m)):
    if i%2==0:
        a.append(m[i])
    else:
        b.append(m[i])
for j in range(len(a)):
    for k in range(1,b[j]+1):
        c.append(a[j])
print(*c)
