for i in range(int(input())):
    z=int(input())
    c=""
    while z:
        if z%2==0:
            c+="0"
        else:
            c+="1"
        z//=2
    print(c[::-1])
    
   