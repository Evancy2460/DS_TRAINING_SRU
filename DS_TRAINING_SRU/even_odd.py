def odev(x,j,s):
    if j==len(l1):
        print(s)
        return
    if l1[j]%2!=0:
        s=s+x+l1[j] 
        l2.append(x+l1[j])
    odev(x,j+1,s)
def oddsum(i):
    if i==len(l):
        return
    if l[i]%2==0:
        odev(l[i],0,0)
    oddsum(i+1)
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
l2=[]
oddsum(0)
print(l2)