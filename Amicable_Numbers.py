a=int(input())
x=int(input())
#b=0
c=[]
for i in range(1,a):
    if a%i==0:
        c.append(i)
b=sum(c)
y=[]
for j in range(1,x):
    if x%j==0:
        y.append(j)
z=sum(y)
if b==x and a==z:
    print("Amicable")
else:
    print("Not Amicable")