s1=input()
s1=s1.lower()
s1=set(s1)
s1=sorted(s1)
s1=''.join(s1)
if 'abcdefghijklmnopqrstuvwxyz' in s1:
    print("yes")
else:
    print("no")
