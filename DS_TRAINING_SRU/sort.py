l1=[1,5,8,9]
l2=[2,7,9,10,14]
i,j=0,0
l3=[]
while(i<len(l1) and j<len(l2)):
    if(l1[i]<l2[j]):
        l3.append(l1[i])
        i+=1
    else:
        l3.append(l2[j])
        j+=1
while j<len(l2):
    l3.append(l2[j])
    j+=1
while i<len(l1):
    l3.append(l1[i])
    i+=1
'''if j<len(l2):
    l3.extend(l2[j:])
if i<len(l1):
    l3.extend(l1[i:])'''
print(l3)
