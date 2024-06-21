def palindrome(n,c,val):
    if n>0:
        k=n%10
        val+=k*(10**c)
        n=n//10
    else:
        return val
    return palindrome(n,c-1,val)
n=int(input())
k,c=n,0
while k>0:
    k=k%10
    c+=1
    k=k//10
l=palindrome(n,c-1,0)
if l==n:
    print("palindrome")
else:
    print("not")
