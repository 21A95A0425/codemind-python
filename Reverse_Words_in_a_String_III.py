z=(input())
a=z.split(' ')
b=[]
for i in a:
    c=i[::-1]
    b.append(c)
print(*b)