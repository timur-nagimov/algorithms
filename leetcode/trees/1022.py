# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root, curr_value=0):
            if root is None:
                return 0

            curr_value = curr_value*2 + root.val
            if root.left is None and root.right is None:
                return curr_value

            left_sum = dfs(root.left, curr_value)
            right_sum = dfs(root.right, curr_value)

            return left_sum + right_sum

        return dfs(root)
