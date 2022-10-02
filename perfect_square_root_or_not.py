z=int(input())
i=1
sq=0
f=False
while sq<=z:
    sq=i*i
    i+=1
    if sq==z:
        f=True
        print(True)
        break
if f==False:
    print(False)