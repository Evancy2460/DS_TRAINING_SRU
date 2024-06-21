s="placements"
for i in s:
    if i in 'aeiou' or i in 'AEIOU':
        print(i.upper(),end="")
    else:
        print(i.lower(),end="")
