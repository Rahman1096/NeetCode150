class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Find first occurrence
        left, right = 0, len(nums) - 1
        first = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if left < len(nums) and nums[left] == target:
            first = left

        # Find last occurrence
        left, right = 0, len(nums) - 1
        last = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        if right >= 0 and nums[right] == target:
            last = right

        return [first, last]