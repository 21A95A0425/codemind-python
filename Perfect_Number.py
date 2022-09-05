a=int(input())
b=[]
for i in range(1,a):
    z=a%i
    if z==0:
        b.append(i)
    c=sum(b)
if a==c:
    print("True")
else:
    print("False")
        