class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []
        
        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(i + 1)
            
            subset.pop()
            backtrack(i + 1)
            
        backtrack(0)
        return res