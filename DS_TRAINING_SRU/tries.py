class node:
    def __init__(self):
        self.data={}
        self.flag=0
        self.pref=0
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,st):
        t=self.root
        for i in st:
            if i not in t.data:
                t.data[i]=node()
            t=t.data[i]
            t.pref+=1
        t.flag=1
    def search(self,st):
        t=self.root
        for i in st:
            if i not in t.data:
                return False
            t=t.data[i]
        if t.flag==1:
            return True
        else:
            return False
    def no_prefix(self,st):
        t=self.root
        for i in st:
            if i not in t.data:
                return 0
            t=t.data[i]
        return t.pref
    def words_prefix(self,st):
        t=self.root
        for i in st:
            if i not in t.data:
                return 0
            t=t.data[i]
        def dfs(s,t):
            if t.flag==1:
                print(s)
                return
            for i in t.data:
                dfs(s+i,t.data[i])
        dfs(st,t)
    def long_prefix(self,st):
        t=self.root
        for i in st:
            if i not in t.data:
                return 0
            t=t.data[i]
        def dfs(s,t,c,m):
            if t.flag==1:
                if c>m:
                    wo=s
                    m=c
                return
            for i in t.data:
                return dfs(s+i,t.data[i],c+1,m)
        return dfs(st,t,len(st),0)
t1=tries()
t1.insert('world')
t1.insert('word')
t1.insert('worst')
t1.insert('world')
t1.insert('apple')
t1.insert('appy')
t1.insert('worried')
print(t1.search('word'))
print(t1.search('world'))
print(t1.search('apple'))
print(t1.search('wrdd'))
print(t1.no_prefix('words'))
t1.words_prefix('wor')
l=['wor','ap']
for i in l:
    print(t1.long_prefix(i))