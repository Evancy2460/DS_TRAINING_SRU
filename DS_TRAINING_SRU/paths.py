def paths(k,i,j,s):
    if i==m-1 and j==n-1:
        return 1
    if i==m or j==n or i==-1 or j==-1 or k[i][j]==1:
        return 0
    k[i][j]=1
    left=paths(k,i,j-1,s)#left
    right=paths(k,i,j+1,s) #right
    top=paths(k,i-1,j,s) #top
    down=paths(k,i+1,j,s) #down
    k[i][j]=0
    return left+right+top+down
m=int(input())
n=int(input())
k=[]
for i in range(m):
    l1=[0]*n
    k.append(l1)
print(paths(k,0,0,[]))