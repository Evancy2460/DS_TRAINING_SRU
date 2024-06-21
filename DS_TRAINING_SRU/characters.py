a="f46feLK9y56u#@&A"
lc=[]
uc=[]
dc,sc,lv,uv=0,0,0,0
for i in range(len(a)):
    if a[i].islower():
        lc.append(a[i])
    elif a[i].isupper():
        uc.append(a[i])
    elif a[i].isdigit():
        dc+=1
    elif not a[i].isalnum():
        sc+=1
v=['a','e','i','o','u']
v1=['A','E','I','O','U']
for i in lc:
    if i in v:
        lv+=1
for i in uc:
    if i in v1:
        uv+=1
print("dc-",dc,"sc-",sc,"lv-",lv,"uv-",uv,"lc-",len(lc)-lv,"uc-",len(uc)-uv)
