z=int(input())
a=z
m={1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}
for i in range(1,z+1):
    for k in range(1,a+1):
        print(m[a],end=" ")
    a-=1
    print()