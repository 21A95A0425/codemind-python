z=int(input())
m=list(map(int,input().split()))
a=[]
b=[]
c=[]
for i in range(len(m)-1):
    if m[i]<m[i+1]:
        f=True
    else:
        f=False
        break
if f==True:
    print("yes")
else:
    print("no")
