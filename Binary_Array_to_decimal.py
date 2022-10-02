z=int(input())
m=list(map(int,input().strip().split()))
s=0
i=0
for i in range(len(m)):
    s=s+(m[i]*(2**z))
    z-=1
print(s//2)
