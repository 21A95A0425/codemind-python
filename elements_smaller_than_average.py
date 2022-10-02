z=int(input())
m=list(map(int,input().strip().split()))
s=0
c=0
for i in range(len(m)):
    s=s+m[i]
avg=s//z
for j in range(len(m)):
    if m[j]<=avg:
        c+=1
print(c)