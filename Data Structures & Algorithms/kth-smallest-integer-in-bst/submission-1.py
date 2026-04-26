class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cmt = collections.deque()

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            self.cmt.append(node.val)
            if len(self.cmt) == k:
                return
            dfs(node.right)

        dfs(root)
        return self.cmt[k-1]