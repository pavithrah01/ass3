class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_height(root):
    if root is None:
        return -1

    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    return 1 + max(left_height, right_height)

# Example usage:
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Calculate the height of the tree
height = tree_height(root)
print("Height of the tree:", height)
