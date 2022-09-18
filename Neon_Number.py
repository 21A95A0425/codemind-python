z=int(input())
m=z*z
s=0
while m!=0:
    r=m%10
    s=s+r
    m=m//10
if s==z:
    print("Neon Number")
else:
    print("Not Neon Number")