s1=input()
s2=input()
s=set(s1+s2)
st=[]
for i in s:
    if i.isdigit():
        st.append(int(i))
st.sort(reverse=True)
if st[-1]%2!=0:
    for i in range(len(st)-1,-1,-1):
        if st[i]%2==0:
            k=st[i]
            st.remove(st[i])
            st.append(k)
            print(*st)
            break
    else:
        print(-1)