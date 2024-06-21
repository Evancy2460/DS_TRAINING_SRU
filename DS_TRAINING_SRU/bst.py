class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class Tree:
    def createNode(self,data):
        return Node(data)
    def insert(self,node,data):
        if node is None:
            return self.createNode(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node
    def sumof(self,root):
        if root==None:
            return 0
        if root!=None:
            return self.sumof(root.left)+root.data+self.sumof(root.right)
    def evensum(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.evensum(root.left)+self.evensum(root.right)
        else:
            return (self.evensum(root.left)+self.evensum(root.right))
    def oddsum(self,root):
        if root==None:
            return 0
        if root.data%2!=0:
            return root.data+self.oddsum(root.left)+self.oddsum(root.right)
        else:
            return (self.oddsum(root.left)+self.oddsum(root.right))
    def absdiff(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.absdiff(root.left)+self.absdiff(root.right)
        else:
            return (self.absdiff(root.left)+self.absdiff(root.right))-root.data
    def traverse_inorder(self,root):
        if root!=None:
            self.traverse_inorder(root.left)
            print(root.data,end=" ")
            self.traverse_inorder(root.right)
    def traverse_preorder(self,root):
        if root!=None:
            print(root.data,end=" ")
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)
    def traverse_postorder(self,root):
        if root!=None:
            self.traverse_postorder(root.left)
            self.traverse_postorder(root.right)
            print(root.data,end=" ")
    def height(self,root):
        if root==None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    def balance(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1
    def leafnodes(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.leafnodes(root.left)+self.leafnodes(root.right)
    def leafnodesum(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.data
        return self.leafnodesum(root.left)+self.leafnodesum(root.right)
    def search(self,root,se):
        if root==None:
            return
        if root.data==se:
            return 1
        if self.search(root.left,se)==1 or self.search(root.right,se)==1:
            return 1
        else:
            return 0
    def depth(self,root,se,c):
        if root.data==se:
            return c
        if root==None:
            return -1
        if root.data>se:
            return self.depth(root.left,se,c+1)
        else:
            return self.depth(root.right,se,c+1)
    def leftview(self,root,c,d):
        if root==None:
            return
        if c not in d:
            d.append(c)
            print(root.data,end=" ")
        self.leftview(root.left,c+1,d)
        self.leftview(root.right,c+1,d)
    def rightview(self,root,c,d):
        if root==None:
            return
        if c not in d:
            d.append(c)
            print(root.data,end=" ")
        self.rightview(root.right,c+1,d)
        self.rightview(root.left,c+1,d)
    def topview(self,root,c,q,d):
        if root==None:
            return
        q.append([root,c])
        while len(q)!=0:
            t=q.pop(0)
            if t[1] not in d:
                d[t[1]]=t[0].data
            if t[0].left!=None:
                q.append([t[0].left,t[1]-1])
            if t[0].right!=None:
                q.append([t[0].right,t[1]+1])
        return d.values()
    def botview(self,root,c,q,d):
        if root==None:
            return
        q.append([root,c])
        while len(q)!=0:
            t=q.pop(0)
            d[t[1]]=t[0].data
            if t[0].left!=None:
                q.append([t[0].left,t[1]-1])
            if t[0].right!=None:
                q.append([t[0].right,t[1]+1])
        return d.values()
    def traverse_level(self,root):
        q=[]
        q.append(root)
        while len(q)!=0:
            root=q.pop(0)
            print(root.data,end=" ")
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
obj=Tree()
root=obj.createNode(5) 
print(root.data)
obj.insert(root,2)
obj.insert(root,11)
obj.insert(root,7)
obj.insert(root,15)
obj.insert(root,12)
obj.insert(root,21)
obj.insert(root,31)
obj.insert(root,6)
obj.insert(root,8)
print("Inorder traversal: ")
obj.traverse_inorder(root)
print()
print("Pre-order traversal: ")
obj.traverse_preorder(root)
print()
print("Post-order traversal: ")
obj.traverse_postorder(root)
print()
print("Height of a tree: ")
print(obj.height(root))
print()
print("Level order traversal: ")
obj.traverse_level(root)
print()
print("Sum of the elements")
print(obj.sumof(root))
print()
print("Even sum:")
print(obj.evensum(root))
print()
print("Odd sum:")
print(obj.oddsum(root))
print()
print("Absolute diff of even and odd")
print(abs(obj.absdiff(root)))
print()
if obj.balance(root):
    print("balanced tree")
else:
    print("Imbalanced tree")
print()
print("No. of leaf nodes",obj.leafnodes(root))
print("Sum of leaf nodes:",obj.leafnodesum(root))
if obj.search(root,21):
    print("Found")
else:
    print("Not found")
print(obj.depth(root,21,0))
print()
print("Left view:")
obj.leftview(root,0,[])
print()
print("Right view:")
obj.rightview(root,0,[])
print()
print("Top view:")
f=obj.topview(root,0,[],{})
print(sorted(f))
print("Bottom view:")
f1=obj.botview(root,0,[],{})
print(sorted(f1))
