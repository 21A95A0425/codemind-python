def p(x):
    s=0
    if x>=3:
        for i in range(2,x):
            if x%i==0:
                s+=1
        if s==0:
            return True
    if x==2:
        return True
    return False
z=int(input())
a=list(map(int,input().split()))
x=int(input())
c=[]
b=[]
for i in range(len(a)):
    if p(a[i])==True:
        b.append(a[i])
for j in range(len(b)):
    if b[j]>=x:
        c.append(b[j])
print(len(c))