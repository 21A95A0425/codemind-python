n=int(input())
for i in range(n):
    a=int(input())
    m=list(map(int,input().split()))
    m.sort()
    for k in range(1,a):
        if m[k-1]!=k:
            print(k)
            break
    else:
        print(k+1)