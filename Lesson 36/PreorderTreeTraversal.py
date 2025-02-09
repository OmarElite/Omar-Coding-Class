class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def DisplayPreorder(node):
    if node == None:
        return
    
    print(node.value, end=" ")
    DisplayPreorder(node.left)
    DisplayPreorder(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder Traversal of binary tree is : ")
DisplayPreorder(root)
