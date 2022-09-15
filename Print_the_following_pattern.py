z=int(input())
d={1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}
if z>0:
    for i in range(1,z+1):
        a=0
        print(" "*(z-i),end="")
        j=2
        for k in range(1,2*i):
            if k<=i:
                print(d[k],end="")
            else:
                print(d[k-j],end="")
                j+=2
        print()