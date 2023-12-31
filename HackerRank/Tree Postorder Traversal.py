class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def find(root):
    global res
    if root is None:
        return
    res.append(root.info)
    
    find(root.right)
    find(root.left)

def postOrder(root):
    global res
    
    #Write your code here
    res = []
    
    find(root)
    
    
    res = res[::-1]
    res2 = ''
    for x in res:
        res2+=' '
        res2+=str(x)
        
    print(res2.strip())


1,2,5,6,3,4



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

postOrder(tree.root)