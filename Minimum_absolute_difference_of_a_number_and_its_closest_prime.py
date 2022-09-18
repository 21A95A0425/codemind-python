z=int(input())
c=0
i=2
k=1
a=2
while True:
    b=a
    while k<=i:
        if i%k==0:
            c+=1
        k+=1
    if c==2:
        a=i
    k=1
    c=0
    if a>=z:
        break
    i+=1
s=abs(b-z)
p=abs(a-z)
print(min(s,p))
    