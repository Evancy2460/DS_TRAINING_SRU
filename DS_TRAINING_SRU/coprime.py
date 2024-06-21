n1=int(input())
n2=int(input())
f=0
r=min(n1//2,n2//2)
for i in range(2,r+1):
    if (n1%i==0) and (n2%i==0):
        print("Not co-prime")
        f=1
        break
if f==0:
    print("Co-prime")
