z=int(input())
m=list(map(int,input().strip().split()))
s=0
c=0
d=0
for i in range(len(m)):
    if d%2!=0:
        s=s+m[i]
    else:
        c=c+m[i]
    d+=1
print(abs(s-c))