l=[2,3,4,1,3,2,4,2,1,3]
c=0
l2=[]
n=len(l)
while(c!=len(l)):
    l1=[]
    for i in range(len(l)):
        if(l[i]>0):  #if(not str(a[i]).isalpha()):
            if l[i] not in l1:
                c+=1
                l1.append(l[i])
                l[i]=-1      #a[i]='a'
    l2.append(l1)
print(l2)