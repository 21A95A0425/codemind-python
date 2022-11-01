n=int(input())
m=list(map(int,input().split()))
k=1
for i in range(len(m)):
    for j in range(len(m)):
        if i==j:
            continue
        k=k*m[j]
    print(k,end=' ')
    k=1