n=input()
r=n[::-1]
if n!=r:
    if len(n)%2==0:
        k1=n[0:len(n)//2]
        s1=k1+k1[::-1]
        if s1<n:
            k1=str(int(k1)+1)
            s1=k1+k1[::-1]
        print(s1)
    else:
        k1=n[0:len(n)//2]
        m=n[(len(n)//2)+1]
        if m<k1[-1]:
            k1=str(int(k1)+1)
            s1=k1+m+k1[::-1]
        else:
            s1=k1+m+k1[::-1]
        print(s1)
else:
    print(n)