class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
            
        rows, cols = len(heights), len(heights[0])
        pac_visited = set()
        atl_visited = set()
        
        def dfs(r, c, visited, prev_height):
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                (r, c) in visited or heights[r][c] < prev_height):
                return
                
            visited.add((r, c))
            
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            
        for c in range(cols):
            dfs(0, c, pac_visited, heights[0][c])
            dfs(rows - 1, c, atl_visited, heights[rows - 1][c])
            
        for r in range(rows):
            dfs(r, 0, pac_visited, heights[r][0])
            dfs(r, cols - 1, atl_visited, heights[r][cols - 1])
            
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac_visited and (r, c) in atl_visited:
                    result.append([r, c])
                    
        return result