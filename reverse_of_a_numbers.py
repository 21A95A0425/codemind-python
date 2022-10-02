z=int(input())
m=len(str(z))
s=0
while z!=0:
    m-=1
    r=z%10
    z=z//10
    s=s+r*(10**m)
print(s)