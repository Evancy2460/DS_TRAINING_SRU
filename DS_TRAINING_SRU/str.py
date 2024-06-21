n=input()
c=0
for i in n:
    if i=='M':
        c+=1
    else:
        c-=1
if c==0:
    print("0")
elif c>0:
    print("Male")
else:
    print("Female")
        
