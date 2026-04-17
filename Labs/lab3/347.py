class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        freq_list = []
        for num, count in counts.items():
            freq_list.append((count, num))
        
        freq_list.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(freq_list[i][1])
            
        return res