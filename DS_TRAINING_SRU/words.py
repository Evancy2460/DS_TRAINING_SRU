st=input().split()
re=[0]*len(st)
for i in st:
    re[int(i[-1])-1]=i[:-1]
print(' '.join(re))
