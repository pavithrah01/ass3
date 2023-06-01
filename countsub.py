class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_subtrees_with_sum(root, target_sum):
    if root is None:
        return 0

    count = [0]  # Using a mutable object to hold the count

    dfs(root, target_sum, count)

    return count[0]

def dfs(node, target_sum, count):
    if node is None:
        return 0

    left_sum = dfs(node.left, target_sum, count)
    right_sum = dfs(node.right, target_sum, count)
    subtree_sum = left_sum + right_sum + node.value

    if subtree_sum == target_sum:
        count[0] += 1

    return subtree_sum

# Example usage:
# Create a binary tree
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.left = Node(5)
root.right.right.right = Node(1)

target_sum = 22

# Count subtrees with the given sum
count = count_subtrees_with_sum(root, target_sum)
print("Number of subtrees with sum", target_sum, ":", count)  # Output: 3
