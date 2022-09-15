a=input()
h=int(a[:2])
m=int(a[3:])
b=abs(30*h-5.5*m)
if b>180:
    b=360-b
print(b)