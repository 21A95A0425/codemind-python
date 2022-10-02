z=int(input())
n=z
b=str(n)
c=len(b)
s=0
while n!=0:
    r=n%10
    n=n//10
    s=s+(r**c)
    c-=1
if s==z:
    print(True)
else:
    print(False)