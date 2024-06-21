st=input()
lc,uc,s,d,c=0,0,0,0,0
l=[]
for i in st:
    if i.islower():
        lc+=1
    elif i.isupper():
        uc+=1
    elif i.isdigit():
        d+=1
    else:
        s+=1
l.append(lc)
l.append(uc)
l.append(d)
l.append(s)
if lc>=1 and uc>=1 and d>=1 and s>=1:
    print(-1)
else:
    for i in l:
        if i==0:
            c+=1
    if c+len(st)>=8:
        print(c)
    else:
        print(8-len(st))
            
        
