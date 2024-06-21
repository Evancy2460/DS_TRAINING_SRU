def maxxi(l1):
    if len(l1)==0:
        return 0
    if len(l1)==1:
        return l1[0]
    if len(l1)==2:
        return max(l1)
    le=l1[0]+maxxi(l1[2:])
    re=l1[1]+maxxi(l1[3:])
    return max(le,re)
l=list(map(int,input().split()))
print(maxxi(l))