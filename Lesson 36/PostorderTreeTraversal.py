class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def DisplayPostorder(node):
    if node == None:
        return
    
    # First recur on left child or left Subtree
    DisplayPostorder(node.left)

    # Recur on right child or right Subtree
    DisplayPostorder(node.right)

    # Display the data of node
    print(node.value, end=" ")

# Node preparation
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Postorder Traversal of binary tree is : ")
DisplayPostorder(root)
