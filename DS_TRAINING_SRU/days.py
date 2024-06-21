l=list(map(int,input().split(" ")))
m=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if (l[j]-l[i])>m:
            m=(l[j]-l[i])
print(m)

'''l=list(map(int,input().split(" ")))
m=0
b,s=l[0],l[0]
for i in range(1,len(l)):
    if l[i]>b and (l[i]-b)>m:
        s=l[i]
        m=s-b
    else:
        b=l[i]
print(m)'''

