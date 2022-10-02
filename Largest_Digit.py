z=int(input())
s=0
while z!=0:
    r=z%10
    z=z//10
    if r>s:
        s=r
print(s)