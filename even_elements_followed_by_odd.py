z=int(input())
m=list(map(int,input().strip().split()))
a=[]
b=[]
for i in range(len(m)):
    if m[i]%2==0:
        a.append(m[i])
    else:
        b.append(m[i])
for j in range(len(b)):
    a.append(b[j])
for k in range(len(a)):
    print(a[k],end=" ")