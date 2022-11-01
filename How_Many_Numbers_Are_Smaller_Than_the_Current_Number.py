n=int(input())
m=list(map(int,input().strip().split()))[:n]
c=0
for i in m:
    for j in m:
        if j<i:
            c+=1
    print(c,end=' ')
    c=0