z=input()
z.casefold()
m=z.split(" ")
v='aeiou'
c=0
a=0
b=0
for i in m:
    for k in i :
        if k in v:
            c+=1
    print(c,end=" ")
    c=0