z,m=map(int,input().split())
s=0
for i in range(z):
    m=list(map(int,input().split()))
    for i in m:
        s+=i
    print(s,end=' ')
    s=0