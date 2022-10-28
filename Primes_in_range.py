import math
def isprime(x):
    z=int(math.sqrt(x))
    if x==1 or x==0:
        return False
    for y in range(2,z+1):
        if x%y==0:return False
    return True
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if isprime(i):
        c+=1
    else:pass
print(c)