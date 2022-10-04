z=input()
z.casefold()
m=z.split(" ")
v='aeiou'
c=0
a=100
b=0
for i in m:
    for k in i :
        if k in v:
            c+=1
    if c<a and c!=0:
        a=c
    c=0
print(a)