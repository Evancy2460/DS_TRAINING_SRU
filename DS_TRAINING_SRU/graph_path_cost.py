def pathscost(d,x,l,y,s):
    l.append(x)
    if x==y:
        print(l,"---->",s)
        s=0
        l.pop()
        return
    for i,k in d[x]:
        if i not in l:
            pathscost(d,i,l,y,s+k)
    l.pop()
def mincost(d,x,l1,y,s,m,l):
    l.append(x)
    if x==y:
        if s<m:
            m=s
            l1=l.copy()
        s=0
        l.pop()
        return m,l1
    for i in d[x]:
        if i[0] not in l:
            m,l1=mincost(d,i,l1,y,s+i[1],m,l)
    l.pop()
    return m,l1
graph={5:[(7,2),(3,6)],
       7:[(5,2),(4,4),(3,2)],
       4:[(7,4),(8,5),(2,6)],
       8:[(3,3),(4,5),(2,4)],
       3:[(5,6),(7,2),(8,3)],
       2:[(4,6),(8,4)]
}
pathscost(graph,5,[],2,0)
print(mincost(graph,5,[],2,0,999,[]))