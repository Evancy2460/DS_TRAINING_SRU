n=int(input())
l=[]
for i in range(n):
    l.append(list(input()))
st=input()
j,k=0,0
for i in st:
    if j==n:
        j=0
    if i not in l[j]:
        k=1
    else:
        l[j].remove(i)
    j+=1
if k==1:
    print("no")
else:
    print("yes")
