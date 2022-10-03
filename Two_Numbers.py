z=int(input())
x=list(map(int,input().split()))
y=[]
j=set(x)
for i in j:
    if x.count(i)==1:
        y.append(i)
y.sort()
print(*y)
