z=int(input())
a=list(map(int,input().split()))
x=int(input())
c=[]
for i in range(x):
    c.append(a[i])
print(sum(c))
