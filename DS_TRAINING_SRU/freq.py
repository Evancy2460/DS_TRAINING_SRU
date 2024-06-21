'''l=list(map(int,input().split()))
s=set(l)
c,m,k=1,0,0
for i in s:
    if i in l:
        c=l.count(i)
        if c>m:
            m=c
            c=1
            k=i
if c>m:
    m=c
    k=i
if m>len(l)//2:
    print(k)'''


l1=list(map(int,input().split()))
c,win=1,l1[0]
for i in l1[1:]:
    if i==win:
        c+=1
    else:
        c=c-1
        if c==0:
            win=i
            c=1
print(win)
    
    
