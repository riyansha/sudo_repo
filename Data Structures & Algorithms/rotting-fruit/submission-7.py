# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
        
#         q = deque()
#         time = 0
#         visited = set()
#         for row in range(len(grid)):
#             for col in range(len(grid[row])):
#                 if grid[row][col] == 2:
#                     q.append((row, col))
#         directions = [(1, 0) , (-1, 0), (0, 1), (0, -1)]
#         while q:
#             i, j = q.popleft()
#             if (i, j) not in visited:
#                 for dx, dy in directions:
#                     ni = i + dx
#                     nj = j + dy
#                     if 0 <= ni < len(grid) and 0 <= nj < len(grid[i]):
#                         if grid[ni][nj] == 1:
#                             grid[ni][nj] = 2
#                             # 
#                             q.append((ni, nj))
#                             visited.add((ni, nj))    #neccessary to keep track of all visited nodes which are 2 or made 2 
                        
#                         else:
#                             continue
#             time = time + 1
#         for row in range(len(grid)):
#             for col in range(len(grid[row])):
#                 if grid[row][col] == 1:
#                     return -1
#         return time
                        
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        time = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    q.append((row, col))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            size = len(q)   # 🔥 process level
            changed = False
            
            for _ in range(size):
                i, j = q.popleft()
                
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                        if grid[ni][nj] == 1:
                            grid[ni][nj] = 2
                            q.append((ni, nj))
                            changed = True
            
            if changed:
                time += 1
        
        # check if any fresh left
        for row in grid:
            if 1 in row:
                return -1
        
        return time
        