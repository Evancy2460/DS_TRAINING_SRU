def dfs(graph,start,l):
    l.append(start)
    for val in graph[start]:
        if val not in l:
            dfs(graph,val,l)
    return l
def paths(d,x,l,y):
    l.append(x)
    if x==y:
        print(l)
        l.pop()
        return
    for i in d[x]:
        if i not in l:
            paths(d,i,l,y)
    l.pop()
graph={5:[7,3],
       7:[5,4,3],
       4:[7,8,2],
       8:[3,4,2],
       3:[5,7,8],
       2:[4,8]
}
print(dfs(graph,5,[]))
print("Paths from 5 to 2:")
paths(graph,5,[],2)

'''{5:[7,3],7:[5,4,3],3:[5,7,8],4:[7,2,8],8:[3,4,2],2:[4,8]}'''