def leng(i):
    if a[i]=='none':
        return i
    return leng(i+1)
a=[1,45,73,22,9]
if leng(0)%2==0:
    print("even")
else:
    print("odd")
