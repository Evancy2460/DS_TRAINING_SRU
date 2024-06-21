n=int(input())
count=0
while n<0:
    k=0
    c=n%10
    for i in range(2,c//2):
        if c%i==0:
            k+=1
            break
    if k==0:
        count+=1
    n=n//10
print(count)
