s1=input().split(",")
l=[]
l1=[]
s2=""
for i in s1:
    l.append(len(i[0:i.index(':')]))
    l1.append(i[i.index(':')+1:])
    if str(l[-1]) in l1[-1]:
        s2=s2+i[i.index(':')-1]
    else:
        for j in range(l[-1]-1,0,-1):
            if str(j) in l1[-1]:
                s2=s2+i[j]
                break
        else:
            s2=s2+'x'
print(s2)

'''hello:5438,car:214,book:8799,apple:2187
oaxp'''