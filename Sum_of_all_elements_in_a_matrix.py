a,b=map(int,input().split())
c=0
for i in range(a):
    x=list(map(int,input().split()))
    for j in x:
        c+=j
print(c)