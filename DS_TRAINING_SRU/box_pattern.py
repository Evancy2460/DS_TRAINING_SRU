n=int(input())
size=(2*n)-1
c=1
for i in range(size):
    for j in range(size):
        x=min(i,j,(size-1)-i,(size-1)-j)
        print(x+1,end=" ")
    print()
