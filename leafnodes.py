class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_leaves(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.value)
    else:
        print_leaves(root.left)
        print_leaves(root.right)

# Example usage:
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

# Print all the leaves
print("Leaf nodes:")
print_leaves(root)
