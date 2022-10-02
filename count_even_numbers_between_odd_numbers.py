z=int(input())
m=list(map(int,input().strip().split()))
c=0
a=0
b=0
d=0
e=0
for i in range(len(m)):
    e+=1
    a=b
    b=c
    c=m[i]
    if a%2!=0 and c%2!=0:
#        if b%2==0:
        d+=1
print(d)