def evod(i,even,odd):
    if i==len(a):
        l=[]
        l.append(even)
        l.append(odd)
        return l
    if a[i]%2==0:
        even+=a[i]
    if b[i]%2!=0:
        odd+=b[i]
    return evod(i+1,even,odd)
a=[3,8,5,4,3]
b=[5,0,9,3,2]
print(tuple(evod(0,0,0))
