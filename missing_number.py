class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num=0
        nums.sort()
        for i in range(max(nums)):
            if num==nums[i]:
                num +=1
            else :
                return num
        return len(nums)  