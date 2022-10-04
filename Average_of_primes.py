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
b=[]
for i in range(len(a)):
    if p(a[i])==True:
        b.append(a[i])
c=sum(b)/len(b)
d="{:.2f}".format(c)
print(d)