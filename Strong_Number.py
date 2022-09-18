z=int(input())
a=z
s=0
p=1
while z:
    r=z%10
    while r:
        p=p*r
        r-=1
    s=s+p
    p=1
    z=z//10
if s==a:
    print("The number",a,"is a strong number")
else:
    print("The number",a,"is not a strong number")