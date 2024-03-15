# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    if not root:
        return 'None'
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))


def deserialize(s):
    def helper(queue):
        val = queue.pop(0)
        if val == 'None':
            return None
        node = Node(val)
        node.left = helper(queue)
        node.right = helper(queue)
        return node
    queue = s.split()
    return helper(queue)


node = Node('root', Node('left', Node('left.left')), Node('right'))
serialized_tree = serialize(node)
deserialized_tree = deserialize(serialized_tree)
assert deserialize(serialize(node)).left.left.val == 'left.left'
