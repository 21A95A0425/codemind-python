a=input()
b=[]
c=["1","2","3","4","5","6","7","8","9","0"]
for i in a:
    if i in c: 
        i=int(i)
        b.append(i)
print(sum(b))