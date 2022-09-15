a=int(input())
s=0
for i in range(1,a+1):
    k=1/(1+(i-1))
    s+=k
print("{:.2f}".format(s))