l=list(map(int,input().split()))
l1=[]
for i in range(len(l)-2):
    if l[i]<l[i+1] and l[i]<l[i+2]:
        l[i]=l[i]
    elif l[i+1]<l[i] and l[i+1]<l[i+2]:
        l[i],l[i+1]=l[i+1],l[i]
    else:
        l[i+2],l[i]=l[i],l[i+2]
    if l[i+1]>l[i+2]:
        l[i+1],l[i+2]=l[i+2],l[i+1]
print(l)