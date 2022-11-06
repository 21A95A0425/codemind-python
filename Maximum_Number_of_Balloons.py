import math
a=input()
b1,a1=0,0
l1=0
o1=0
n1=0
for i in a:
    if i=="b":
        b1+=1
    elif i=="a":
        a1+=1
    elif i=="l":
        l1+=0.5
    elif i=="o":
        o1+=0.5
    elif i=="n":
        n1+=1
l1=math.floor(l1)
o1=math.floor(o1)
print(min(b1,a1,l1,o1,n1))