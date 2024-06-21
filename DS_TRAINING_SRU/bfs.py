graph={5:[7,3],
       7:[5,4,3],
       4:[7,8,2],
       8:[3,4,2,9],
       3:[5,7,8],
       2:[4,8],
       9:[8]
}
que,vis=[],[]
que.append(5)
while(len(que)!=0):
    for val in graph[que[0]]:
        if val not in que and val not in vis:
            que.append(val)   
    vis.append(que.pop(0))
print(vis)