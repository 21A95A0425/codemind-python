z,k=map(int,input().split())
m=list(map(int,input().split()))
g=[]
s=0
count=0
for i in range(len(m)):
    c=abs(m[i])
    a=str(c)
    b=len(a)
    if b==k:
        s+=1
print(s)
