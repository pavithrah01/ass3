class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_odd_level_nodes(root):
    if root is None:
        return

    dfs(root, 1)

def dfs(node, level):
    if node is None:
        return

    if level % 2 != 0:
        print(node.value)

    dfs(node.left, level + 1)
    dfs(node.right, level + 1)

# Example usage:
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Print nodes at odd levels
print("Nodes at odd levels:")
print_odd_level_nodes(root)  # Output: 1, 4, 5, 7
