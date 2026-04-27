class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def bfs(row, col, grid):
            q = collections.deque([(row, col, 0)])  # include distance
            # visited = set()
            visited = set([(row, col)])
            while q:
                i, j, dist = q.popleft()
                if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                    continue
                if grid[i][j] == -1:
                    # q.popleft()
                    continue
                if grid[i][j] == 0:
                        grid[row][col] = dist
                        return
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ni, nj = i + dx, j + dy
                    if (ni, nj) not in visited:
                        visited.add((ni, nj))
                        q.append((ni, nj, dist + 1))
                # else:
                #     count += 1
                # visited.append((i, j))

                
                
                # if grid[i][j] == 2147483647 and (i, j) not in visited:
                #     q.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
                #     visted.append((i, j))
           
                
           
                
       
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2147483647:
                    bfs(i, j, grid)
             
  

    
        