a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=0
for i in y:
    if i in x:
        z+=1
        c=x.index(i)
        x.pop(c)
    else:
        break
if z==len(y):
    print("Yes")
else:
    print("No")