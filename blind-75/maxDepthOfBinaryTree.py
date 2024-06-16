# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        def depthFinder(node, count):
            if not node:
                return count
            else:
                count += 1
                return max(depthFinder(node.left, count), depthFinder(node.right, count))
        
        return depthFinder(root, 0)