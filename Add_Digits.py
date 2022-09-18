z=int(input())
s=0
while True:
    r=z%10
    s=s+r
    z=z//10
    if z==0 and s>9:
        z=s
        s=0
    if z==0 and s<10:
        print(s)
        break