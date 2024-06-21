l=list(map(int,input().split()))
n=int(input())
m=[]
for i in range(len(l)):
    l1=[0]*(n+1)
    m.append(l1)
for i in range(len(l)):
    for j in range(n+1):
        if j==0 or j==l[i]:
            m[i][j]=1
        elif j<l[i]:
            m[i][j]=m[i-1][j]
        else:
            k=j-l[i]
            if m[i-1][k]==1 or m[i-1][j]==1:
                m[i][j]=1
print(m)
if m[len(l)-1][n]==1:
    print("True")
else:
    print("False")