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
        if root is None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
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
obj.insert(root,10)
obj.insert(root,7)
obj.insert(root,15)
obj.insert(root,12)
obj.insert(root,20)
obj.insert(root,30)
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