class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        f = 0
        for i in range(n):
            f += i * nums[i]
        
        max_f = f
        for i in range(1, n):
            f = f + total_sum - n * nums[n-i]
            max_f = max(max_f, f)
        
        return max_f