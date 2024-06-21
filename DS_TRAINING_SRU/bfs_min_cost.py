graph={5:[(7,2),(3,6)],
       7:[(5,2),(4,4),(3,2)],
       4:[(7,4),(8,5),(2,6)],
       8:[(3,3),(4,5),(2,4)],
       3:[(5,6),(7,2),(8,3)],
       2:[(4,6),(8,4)]}
d={5:9999,7:9999,4:9999,8:9999,3:9999,2:9999}
que,vis=[5],[]
d[5]=0
while(que):
    m=9999
    for i in que:
        if (d[i]<m):
            m=d[i]
            x=i
    for val in graph[x]:
        if val[0] not in vis:
            if d[val[0]]>d[x]+val[1]:
                d[val[0]]=d[x]+val[1]
            que.append(val[0])   
    vis.append(que.pop(0))
print(d)