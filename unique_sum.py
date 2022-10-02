z=int(input())
m=list(map(int,input().strip().split()))[:z]
a=[]
s=0
for i in range(len(m)):
    if m[i] not in a:
        a.append(m[i])
for j in range(len(a)):
    s=s+a[j]
print(s)