n=int(input())
k=n/2+1
for i in range(n):
    a=97
    print("_"*k,end=" ")
    for j in range(2*i+1):
        print(a)
        a=a+1
    for k1 in range(2*i):
        a=a-1
        print(a)
        print(" "*k,end=" ")
    k-=1
    print()
