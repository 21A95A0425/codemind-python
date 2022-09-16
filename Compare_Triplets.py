x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=0
d=0
for i in range(len(x)):
    if x[i]>y[i]:
        c+=1
    if x[i]<y[i]:
        d+=1
print(c,d)        