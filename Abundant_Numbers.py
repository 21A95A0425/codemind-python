a=int(input())
#b=0
c=[]
for i in range(1,a):
    if a%i==0:
        c.append(i)
b=sum(c)
if b>a:
    print("True")
else:
    print("False")