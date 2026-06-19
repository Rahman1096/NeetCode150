class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        #range can be [-k,k] for each index
        score=max(nums)-k -(min(nums)+k)# equals to acore =max(nums)-min(nums)-2*k
        #if range overlaps return 0 coz some number cancels out 
        return max(0,score)