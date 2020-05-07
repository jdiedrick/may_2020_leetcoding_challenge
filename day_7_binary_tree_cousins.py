# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        valid_nodes = []

        def traverse(node, value, depth, parent):
            if node:
                if node.val == value:
                    valid_nodes.append( (depth, parent) ) # why can't i just return here?
                depth += 1
                parent = node.val
                traverse(node.left, value, depth, parent)
                traverse(node.right, value, depth, parent)

        traverse(root, x, 0, None)
        traverse(root, y, 0, None)

        x_node, y_node = valid_nodes[0], valid_nodes[1]
        x_node_depth, x_node_parent = x_node[0], x_node[1]
        y_node_depth, y_node_parent = y_node[0], y_node[1]

        if x_node_depth == y_node_depth and x_node_parent != y_node_parent:
            return True
        else:
            return False
