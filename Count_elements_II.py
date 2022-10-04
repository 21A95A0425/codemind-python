a,b=map(int,input().split())
m=list(map(int,input().split()))[:a]
y=list(map(int,input().split()))[:b]
a=[]
b=[]
c=0
for i in m:
    if i not in a:
        a.append(i)
for j in y:
    if j not in b:
        b.append(j)
for k in a:
    if k not in b:
        c+=1
for h in b:
    if h not in a:
        c+=1
print(c)
