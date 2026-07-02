class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            # expand in right
            window_sum += nums[right]

            while window_sum >=target:
                # update answer
                min_len = min(min_len, right-left+1)
                # shrink in left
                window_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0