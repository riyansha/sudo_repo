"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#need to keep a visited variable
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         q = collections.deque()
#         res = []
#         if node.val is not None:
#             q.append(node)
#         while q:
#             node = q.popleft()
#             if node.neighbors != None:
#                 for i in range(len(node.neighbors)):
#                     clone = []
#                     clone.append(node.neighbors[i].val)
#                     q.append(node.neighbors[i])
            
#             else:
#                 clone = []
#                 res.append(clone)
import collections

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        q = collections.deque([node])

        # ✅ mapping: original → clone
        clones = {node: Node(node.val)}

        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
                if nei not in clones:
                    # create clone
                    clones[nei] = Node(nei.val)
                    q.append(nei)

                # connect neighbors
                clones[curr].neighbors.append(clones[nei])

        return clones[node]

