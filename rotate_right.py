class Solution:
    def reversal(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)

        # reverse entire array
        self.reversal(nums, 0, len(nums) - 1)

        # reverse first k elements
        self.reversal(nums, 0, k - 1)

        # reverse remaining elements
        self.reversal(nums, k, len(nums) - 1)