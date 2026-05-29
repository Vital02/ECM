class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for crc, pre in prerequisites:
            adj[pre].append(crc)
            
        visit = [0] * numCourses
        
        def has_cycle(v):
            if visit[v] == 1:
                return True
            if visit[v] == 2:
                return False
                
            visit[v] = 1
            
            for neighbor in adj[v]:
                if has_cycle(neighbor):
                    return True
                    
            visit[v] = 2
            return False
            
        for i in range(numCourses):
            if has_cycle(i):
                return False
                
        return True