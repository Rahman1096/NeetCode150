class Solution:
    def topKFrequent(self, nums, k):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        sorted_items = sorted(
            freq.items(),
            key=lambda item: item[1],
            reverse=True
        )

        

        return [key for key, value in sorted_items[:k]]