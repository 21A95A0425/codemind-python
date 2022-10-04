z=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
x=z//2
for i in range(x):
    b.append(a[i])
for j in a:
    if j not in b:
        c.append(j)
print(sum(b))
print(sum(c))