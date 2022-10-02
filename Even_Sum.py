z=int(input())
m=list(map(int,input().strip().split()))
s=0
c=0
d=0
for i in range(len(m)):
    if m[i]%2==0:
        s=s+m[i]
print(s)