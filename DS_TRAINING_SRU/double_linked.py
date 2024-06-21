class node:
    def __init__(self,val=0):
        self.val=val
        self.prev=None
        self.next=None
class sas:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbegin(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.head.prev=new
            new.next=self.head
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            t=node(data)
            self.tail.next=t
            t.prev=self.tail
            self.tail=self.tail.next
    def printing(self):
        temp=self.head
        while(temp):
            print(temp.val,end=" ")
            temp=temp.next
        print()
    def reverse(self):
        temp=self.tail
        while(temp):
            print(temp.val,end=" ")
            temp=temp.prev
        print()
    def linear_search(self,x):
        temp=self.head
        while(temp!=None):
            if x==temp.val:
                print("Found")
                return 
            temp=temp.next
        print("Not found")
    def search(self,x):
        t1=self.head
        t2=self.tail
        while t1.prev!=t2 and t1!=t2:
            if (t1.val==x or t2.val==x):
                print("Found")
                return
            t1=t1.next
            t2=t2.prev
        if t1.val==x:
            print("Found")
            return
        print("Not Found")
    def length(self):
        t1=self.head
        t2=self.tail
        while(t1.prev!=t2 and t1!=t2):
            t1=t1.next
            t2=t2.prev
        if t1==t2:
            print("Odd length")
        else:
            print("Even length")
    def palindrome(self):
        t1=self.head
        t2=self.tail
        while(t1!=t2 and t1.prev!=t2):
            if t1.val!=t2.val:
                print("Not a palindrome")
                return
            t1=t1.next
            t2=t2.prev
        print("Palindrome")
    def half(self):
        f=self.head
        s=self.head
        while(f!=None and f.next!=None):
            f=f.next.next
            s=s.next
        self.tail.next=self.head
        self.head.prev=self.tail
        self.tail=s.prev
        s.prev.next=None
        s.prev=None
        self.head=s
    def swap(self):
        t1=self.head
        t2=self.head.next
        self.head=t2
        while t1!=None:
            t1.prev,t2.prev=t2.prev,t1.prev
            t1.next,t2.next=t2.next,t1.next
            t1=t1.next
            t2=t1.next
    '''def parenthesis(self):
        l2=[]
        f,c=0,0
        temp=self.head
        while(temp!=None):
            if temp.val=='(' or temp.val=='[' or temp.val=='{':
                l2.append(temp.val)
            elif l2[-1]=='{' and temp.val=='}':
                l2.pop()
            elif l2[-1]=='[' and temp.val==']':
                l2.pop()
            elif l2[-1]=='(' and temp.val==')':
                l2.pop()
            else:
                f=1
                print(c+1)
                return
            temp=temp.next
            c+=1
        if f==0:
            print("-1")'''
    def evoddsum(self,temp,es,os):
        if temp==None:
            return es-os
        if temp.val%2==0:
            es+=temp.val
        else:
            os+=temp.val
        temp=temp.next
        return self.evoddsum(temp,es,os)
    def prime(self,temp,c):
        if temp==None:
            return c
        def pri(data,i=2):
            if i>data//2:
                return 1
            if data%i==0 or data<=1:
                return 0
            return pri(data,i+1)
        if pri(temp.val):
            c+=1
        return self.prime(temp.next,c)
l1=sas()
l1.insertatbegin(1)
l1.insertatbegin(31)
l1.insertatbegin(3)
l1.insertatbegin(40)
l1.insertatend(5)
l1.insertatend(60)
l1.insertatend(7)
l1.insertatend(7)
l1.printing()
l1.reverse()
l1.linear_search(100)
l1.search(10)
l1.length()
l1.palindrome()
l1.half()
l1.printing()
l1.reverse()
#l1.swap()
l1.printing()
print(l1.evoddsum(l1.head,0,0))
print(l1.prime(l1.head,0))
'''l1.insertatbegin(']')
l1.insertatbegin('{')
l1.insertatbegin(')')
l1.insertatbegin('(')
l1.insertatbegin('[')
l1.insertatbegin('[')
l1.printing()
l1.parenthesis()'''