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
    if c>a:
        a=c
    c=0
    
for j in m:
    for z in j:
        if z in v:
            c+=1
    if c==a:
        b+=1
    c=0
print(b)