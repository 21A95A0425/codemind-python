z=(input())
m=(input())
s=''
p=''
s=z+m
a=list(s)
a.sort()
for i in range(len(a)):
    p=p+a[i]
print(p)