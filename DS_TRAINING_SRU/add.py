s=input()
l=list(map(float,s.split(" ")))
even,odd,dec=0.0,0.0,0.0
for i in l:
    if not i.is_integer():
        dec+=i
    elif i%2==0.0:
        even+=i
    else:
        odd+=i
print(even,odd,dec)
