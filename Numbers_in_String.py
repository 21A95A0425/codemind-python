z=input()
sum=0
for i in z:
    if i.isdigit():
        i=int(i)
        sum+=i
print(sum)