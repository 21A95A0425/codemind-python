a,b,c=map(int,input().split())
d=[]
for i in range(a,b+1):
    if i%c==0:
        d.append(i)
print(len(d))
    