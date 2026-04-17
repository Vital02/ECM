class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for i in strs:
            s = "".join(sorted(i))
            if s not in groups:
                groups[s] = []
            groups[s].append(i)
            
        return list(groups.values())