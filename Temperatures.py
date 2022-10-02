z=int(input())
m=list(map(int,input().strip().split()))[:z]
c=0
f=False
for i in range(len(m)):
    f=False
    for j in range(len(m)):
        if j<=i:
            continue
        c+=1
        if m[j]>m[i]:
            f=True
            print(c,end=" ")
            break
    if f==False:
        print(0,end=" ")
    c=0
