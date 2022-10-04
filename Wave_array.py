z=int(input())
m=list(map(int,input().split()))
a=[]
b=[]
c=[]
f=True
for i in range(len(m)):
    if i%2==0:
        a.append(m[i])
    else:
        b.append(m[i])
if a[0]>b[0]:
    for k in range(z//2):
        if a[k]>b[k]:
            f=True
        else:
            f=False
            break
else:
    for j in range(len(m)//2):
        if a[j]<b[j]:
            f=True
        else:
            f=False
            break
if f==True:
    print("yes")
else:
    print("no")
