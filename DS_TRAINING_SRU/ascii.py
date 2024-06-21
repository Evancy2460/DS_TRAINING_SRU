n=input()
k=int(input())
l=k%26
'''no. of jumps'''
s=""
for i in n:
    if((ord(i)-l)<97):
        s=s+chr(ord(i)-l+26)
    else:
        s=s+chr(ord(i)-l)
print(s)
            
