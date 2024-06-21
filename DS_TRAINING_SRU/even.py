def even(x):
    if x==0:
        return 0
    return x+even(x-2)
n=13
if n%2==0:
    print(even(n))
else:
    print(even(n-1))
    


