a,b=map(int,input().split())
z=0
x=list(map(int,input().split()))
for i in range(a):
    for j in range(i+1,a+1):
        if b==sum(x[i:j]):
            z+=1
print(z)