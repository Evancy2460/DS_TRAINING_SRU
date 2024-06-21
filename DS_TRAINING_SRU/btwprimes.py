def is_prime(x,y):
    if x<y:
        return 0
    for i in range(2,x//2+1):
        if x%i==0:
            return is_prime(x-1,y)
    else:
        return x

l=list(map(int,input().split()))
y=0
for i in range(len(l)-1):
    y+=is_prime(l[i+1],l[i])
print(y)