n,k=map(int,input().split())
m=list(map(int,input().split()))
c=0
for i in range(len(m)):
    if m[i]%k:
        c+=1
print(c)