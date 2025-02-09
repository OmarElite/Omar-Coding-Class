class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def DisplayInorder(root):
    if root:
        # First Recur on left Child
        DisplayInorder(root.left)

        # Display the data of the node tree
        print(root.value, end=" ")

        # Recur on the right Child
        DisplayInorder(root.right)

# Node preparation
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal of binary tree is : ")
DisplayInorder(root)
