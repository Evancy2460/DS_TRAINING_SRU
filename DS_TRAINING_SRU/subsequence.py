def seq(x,j):
    l.append(x)
    for k in range(j+1,len(a)):
        seq(x+a[k],k)
a="abcd"
l=[]
for i in range(len(a)):
    seq(a[i],i)
print(l)