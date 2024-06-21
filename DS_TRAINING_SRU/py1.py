n=int(input())
size=(2*n)-1
c=97
for i in range(n):
    for j in range(size):
        if ((i+j)<(n-1)) or ((j-i)>=n):
            print("_",end=" ")
        elif j==(size//2):
            print(chr(c+i),end=" ")
        elif ((j-i)-(size//2))<n:
            print(chr(c+((j-i)-(size//2))),end=" ")
        else:
            print(chr(c+(i+j)-(size//2)),end=" ")
    print()
