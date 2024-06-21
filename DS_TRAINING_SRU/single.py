def prime(c):
    l=[2,3,5,7]
    if c in l:
        return 1
    else:
        return 0
def cou(n):
    c=0
    while n>0:
        c+=(n%10)
        n=n//10
    if c<10:
        return c
    return cou(c)
n=int(input())
k=n
c1=cou(n)
while (prime(c1)!=1):
    k+=1
    c1=cou(k)
print(k)   
