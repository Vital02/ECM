class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        old_to_new = {}
        
        def dfs(curr_node):
            if curr_node in old_to_new:
                return old_to_new[curr_node]
                
            copy = Node(curr_node.val)
            old_to_new[curr_node] = copy
            
            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
            
        return dfs(node)