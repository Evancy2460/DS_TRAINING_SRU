n=int(input())
l,st,c=set(),"",0
for i in range(n):
    s=input()
    if s[0]=='1':
        l.add(s[2:])
    elif s[0]=='2':
        if s[2:] in l:
            st=st+" True"
        else:
            st=st+" False"
    elif s[0]=='3':
        k=len(s)-2
        for i in l:
            if s[2:]==i[0:k]:
                c+=1
        st=st+" "+str(c)
    else:
        l.remove(s[2:])
print(st)














