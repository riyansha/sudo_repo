class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def preOrder(node, min_val, max_val):
            if not node:
                return True
            else:
                if not (min_val < node.val < max_val):
                    return False
                return preOrder(node.left, min_val, node.val) and preOrder(node.right, node.val, max_val)
        
        return preOrder(root, float('-inf'), float('inf'))
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
        
#         def dfs(node, low, high):
#             if not node:
#                 return True
            
#             if not (low < node.val < high):
#                 return False
            
#             return (
#                 dfs(node.left, low, node.val) and
#                 dfs(node.right, node.val, high)
#             )
        
#         return dfs(root, float("-inf"), float("inf"))