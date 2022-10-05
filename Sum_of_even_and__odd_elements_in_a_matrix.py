a,b=map(int,input().split())
c=[]
d=[]
o=[]
e_sum,o_sum=0,0
for _ in range(a):
    c.append(list(map(int,input().split())))
for i in range(a):
    for j in range(b):
        d.append(c[i][j])
e=[x for x in d if x%2==1]
f=[x for x in d if x%2==0]
print(sum(f),sum(e))