def p(x):
    c=0
    if x>=3:
        for i in range(2,x):
            if x%i==0:
                c+=1
        if c==0:
            return True
    if x==2:
        return True
    return False
n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    if p(i)==True:
        s+=1
print(s)