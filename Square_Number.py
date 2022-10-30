def square(z):
    a=int(z*0.5)
    for i in range(1,a+1):
        if (i*i)==z:
            return True
    return False
z=int(input())
res=square(z)
print(res)