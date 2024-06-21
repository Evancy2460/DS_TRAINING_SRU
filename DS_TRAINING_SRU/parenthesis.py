l1="[(){}{()}]"
l2=[]
f=0
for i in l1:
    if i=='(' or i=='[' or i=='{':
        l2.append(i)
    elif l2[-1]=='{' and i=='}':
        l2.pop()
    elif l2[-1]=='[' and i==']':
        l2.pop()
    elif l2[-1]=='(' and i==')':
        l2.pop()
    else:
        f=1
        print(l1.index(i))
        break
if f==0:
    print("-1")
