# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def __init__(self, count=0):
#         self.count = count
#     def goodNodes(self, root: TreeNode) -> int:
#         if not root:
#             return self.count
#         else:
#             if root.left != None:
#                 if root.left.val > root.val:
#                     self.count = self.count + 1
#                 self.goodNodes(root.left)
#             if root.right != None:
#                 if root.right.val > root.val:
#                     self.count = self.count + 1
#                 self.goodNodes(root.right)
#             self.count = self.count + 1   # to account for the root case
#         return self.count
class Solution:
    def __init__(self):
        self.count = 0

    def goodNodes(self, root: TreeNode, max_so_far=float("-inf")) -> int:
        if not root:
            return self.count

        # ✅ check current node against max_so_far (not parent)
        if root.val >= max_so_far:
            self.count += 1
            max_so_far = root.val

        # ✅ pass updated max_so_far down the tree
        self.goodNodes(root.left, max_so_far)
        self.goodNodes(root.right, max_so_far)

        return self.count

                



        