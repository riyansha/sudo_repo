class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # class Solution:
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # visited = set()
        # for i in range(len(prerequisites)):
        #     # for j in range(prerequisites[i]):
        #     if tuple(sorted(prerequisites[i])) in visited: #means cycle returned by list
        #         return False
        #     else:
        #         visited.add(tuple(prerequisites[i]))
        # return True
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:   #each pair
            preMap[crs].append(pre)
        taken = []
        #visitset = all courses along current dfs path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []: 
                #no prerequistes
                if crs not in taken:
                    taken.append(crs)
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            taken.append(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return []
        return taken
        # for crs in range(numCourses):
        #     valid = dfs(crs)
        #     taken.append(valid)
        # if len(taken) == 0: return []
        # return taken




                                     
                              
        
        