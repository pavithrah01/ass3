class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(root):
    if root is None:
        return []

    result = [root.value]
    result += preorder_traversal(root.left)
    result += preorder_traversal(root.right)

    return result

def inorder_traversal(root):
    if root is None:
        return []

    result = inorder_traversal(root.left)
    result.append(root.value)
    result += inorder_traversal(root.right)

    return result

def postorder_traversal(root):
    if root is None:
        return []

    result = postorder_traversal(root.left)
    result += postorder_traversal(root.right)
    result.append(root.value)

    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Perform pre-order traversal
preorder = preorder_traversal(root)
print("Pre-order traversal:", preorder)  # Output: [1, 2, 4, 5, 3]

# Perform in-order traversal
inorder = inorder_traversal(root)
print("In-order traversal:", inorder)  # Output: [4, 2, 5, 1, 3]

# Perform post-order traversal
postorder = postorder_traversal(root)
print("Post-order traversal:", postorder)  # Output: [4, 5, 2, 3, 1]
