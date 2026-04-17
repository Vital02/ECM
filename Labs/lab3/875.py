class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high
        
        while low <= high:
            k = (low + high) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
                
            if hours <= h:
                res = k
                high = k - 1
            else:
                low = k + 1
                
        return res