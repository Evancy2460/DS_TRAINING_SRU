def prime(n):
    k=0
    for i in range(2,n//2):
        if n%i==0:
            k+=1
            break
    if k==0:
        print(n)
    else:
        n+=1
        prime(n)
n=int(input())
prime(n)
        


