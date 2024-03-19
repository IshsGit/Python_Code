# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_unival_subtrees(root):
    count = 0

    def is_unival(root):
        nonlocal count
        if not root:
            return True

        left_unival = is_unival(root.left)
        right_unival = is_unival(root.right)

        if left_unival and right_unival:
            if (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
                count += 1
                return True

        return False

    is_unival(root)
    return count


# Example usage:
# Construct the example binary tree
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(0)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(1)

# Count the number of unival subtrees
print(count_unival_subtrees(root))  # Output: 5
