class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_left_leaves(root):
    if root is None:
        return 0

    left_sum = 0

    # Check if the left child is a leaf node
    if root.left and root.left.left is None and root.left.right is None:
        left_sum += root.left.value

    left_sum += sum_left_leaves(root.left)  # Recursive call on the left subtree
    left_sum += sum_left_leaves(root.right)  # Recursive call on the right subtree

    return left_sum

# Example usage:
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Calculate the sum of left leaves
sum_of_left_leaves = sum_left_leaves(root)
print("Sum of left leaves:", sum_of_left_leaves)  # Output: 4 + 5 = 9
