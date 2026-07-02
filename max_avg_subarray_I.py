class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[0:k])
        max_avg =window_sum/k
        for i in range(1,len(nums)-k+1):
            window_sum -=nums[i-1]
            window_sum +=nums[k+i-1]
            max_avg= max(max_avg,window_sum/k)
        return max_avg