n=int(input())
l1=list(map(int,input().split()))
for i in range(n+1):
    if i not in l1:
        print(i)
        break
