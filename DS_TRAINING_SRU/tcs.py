str1=input()
n=int(input())
s1=""
for i in range(n):
    b=input()
    if (b[0]=='L'):
        s1=s1+str1[int(b[2])]
    else:
        s1=s1+str1[-int(b[2])]
print(s1)
l2=[]
for i in range((len(str1)-n)+1):
    l2.append(str1[i:(i+n)])
print(l2)
f=0
for i in l2:
    if sorted(i)==sorted(s1):
        print("yes")
        f=1
        break
if f==0:
    print("no")
    