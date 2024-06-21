n=input()
c,m=1,0
for i in range(len(n)-1):
    if ord(n[i])==ord(n[i+1])-1:
        c+=1
    else:
        if c>m:
            m=c
        c=1
if c>m:
    m=c
print(m)        
    
