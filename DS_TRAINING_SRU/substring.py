'''st=input()
c,m=1,0
st1=""
for i in range(len(st)):
    for j in range(i,len(st)):
        if st[j] in st1:
            if c>m:
                m=c
            c=1
            st1=""
            break
        st1=st1+st[j]
        c+=1
if c>m:
    m=c
print(m-1)'''
a="abfgresagtyuiofde"
d={}
s=""
m=0
i=0
while(i<len(a)):
    while (i<len(a)):
        if(a[i] not in s):
            s=s+a[i]
            d[s[i]]=i
        else:
            if(len(s)>m):
                m=len(s)
            s=''
            break
    i=d[s[i]]+1
print(m)