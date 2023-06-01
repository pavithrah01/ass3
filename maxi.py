from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_level_sum(root):
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    max_sum = float('-inf')

    while queue:
        level_sum = 0
        level_size = len(queue)

        for _ in range(level_size):
            current_node = queue.popleft()
            level_sum += current_node.value

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        max_sum = max(max_sum, level_sum)

    return max_sum

# Example usage:
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

# Find the maximum level sum
max_sum = max_level_sum(root)
print("Maximum level sum:", max_sum)  # Output: 12 (Level 2: 4 + 5 + 3)

