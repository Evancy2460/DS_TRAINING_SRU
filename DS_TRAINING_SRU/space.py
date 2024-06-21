def fact(n,k,i):
    if k==0:
        return i+1
    if n%i==0 and k!=0:
        k-=1
    i=i-1
    return fact(n,k,i)
n=int(input())
k=int(input())
print(fact(n,k,n))
