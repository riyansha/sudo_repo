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