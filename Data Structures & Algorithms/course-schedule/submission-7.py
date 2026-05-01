class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        #visitset = all courses along current dfs path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []: #no prerequistes
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True




                                     
                              
        