z=input()
stg=z.split(" ")
a=0
for i in range(len(stg)):
    c=len(stg[i])
    if c>a:
        a=c
print(a)