l=list(map(int,input().split()))
m1,c=l[0],1
for i in range(1,len(l)):
    if l[i]>m1:
        m1=l[i]
        c+=1
print(c)
m1,c=l[len(l)-1],1
for i in range(-2,-len(l)+1,-1):
    if l[i]>m1:
        m1=l[i]
        c+=1
print(c)