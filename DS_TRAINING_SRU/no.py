str="aaabbaaaadddb"
k=0
for i in range(len(str)):
    if i==len(str)-1:
        print(str[i],k+1)
    else:
        if(str[i]==str[i+1]):
            k+=1
        else:
            print(str[i],k+1)
            k=0
str="aaabbaaaadddb"
k=1
str1=''
for i in range(len(str)-1):
    if(str[i]==str[i+1]):
        k=k+1
    else:
        str1=str1+str[i]+k
        k=1
    
        
