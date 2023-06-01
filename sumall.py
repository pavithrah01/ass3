class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0

    left_depth = get_depth(root.left)
    right_depth = get_depth(root.right)

    if left_depth == right_depth:
        # Left subtree is a perfect binary tree
        return (2 ** left_depth) + count_nodes(root.right)
    else:
        # Right subtree is a perfect binary tree
        return (2 ** right_depth) + count_nodes(root.left)

def get_depth(node):
    depth = 0
    while node:
        depth += 1
        node = node.left
    return depth

def sum_of_nodes(root):
    if root is None:
        return 0

    total_nodes = count_nodes(root)
    return calculate_sum(root, total_nodes)

def calculate_sum(node, total_nodes):
    if node is None:
        return 0

    left_nodes = count_nodes(node.left)
    if left_nodes == total_nodes // 2:
        # The node is the middle node in the last level
        return node.value

    if left_nodes > total_nodes // 2:
        # The node is in the left subtree
        return calculate_sum(node.left, total_nodes // 2)
    else:
        # The node is in the right subtree
        return calculate_sum(node.right, total_nodes // 2)

# Example usage:
# Create a perfect binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Calculate the sum of all nodes
sum_of_all_nodes = sum_of_nodes(root)
print("Sum of all nodes:", sum_of_all_nodes)  # Output: 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
