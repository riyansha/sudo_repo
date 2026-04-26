# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right   #go down the right subtree as oth lies in right subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr     #means either one is itself eqqual to curr.val or both lies in differnt subtree from root as curr
