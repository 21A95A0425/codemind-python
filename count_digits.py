z=int(input())
m=list(map(int,input().split()))
g=[]
s=0
count=0
for i in range(len(m)):
    c=abs(m[i])
    a=str(c)
    b=len(a)
    print(b,end=" ")
