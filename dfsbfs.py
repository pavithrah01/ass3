class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    if root is None:
        return []

    queue = [root]
    result = []

    while queue:
        current_node = queue.pop(0)
        result.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

    return result

def dfs_preorder(root):
    if root is None:
        return []

    result = [root.value]
    result += dfs_preorder(root.left)
    result += dfs_preorder(root.right)

    return result

def dfs_inorder(root):
    if root is None:
        return []

    result = dfs_inorder(root.left)
    result.append(root.value)
    result += dfs_inorder(root.right)

    return result

def dfs_postorder(root):
    if root is None:
        return []

    result = dfs_postorder(root.left)
    result += dfs_postorder(root.right)
    result.append(root.value)

    return result

# Example usage:
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

# Perform BFS traversal
bfs_result = bfs(root)
print("BFS traversal:", bfs_result)  # Output: [1, 2, 3, 4, 5, 6]

# Perform DFS (preorder) traversal
dfs_preorder_result = dfs_preorder(root)
print("DFS (preorder) traversal:", dfs_preorder_result)  # Output: [1, 2, 4, 5, 3, 6]

# Perform DFS (inorder) traversal
dfs_inorder_result = dfs_inorder(root)
print("DFS (inorder) traversal:", dfs_inorder_result)  # Output: [4, 2, 5, 1, 6, 3]

# Perform DFS (postorder) traversal
dfs_postorder_result = dfs_postorder(root)
print("DFS (postorder) traversal:", dfs_postorder_result)  # Output: [4, 5, 2, 6, 3, 1]
