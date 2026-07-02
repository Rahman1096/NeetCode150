class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avgs = [-1] * n

        # Window size is larger than the array
        if 2 * k + 1 > n:
            return avgs

        # Initial window sum
        total = sum(nums[:2 * k + 1])

        for i in range(k, n - k):

            # 1. Calculate the average BEFORE sliding
            avgs[i] = total // (2 * k + 1)

            # 2. Don't slide after the last window
            if i < n - k - 1:
                # Leaving window
                total -= nums[i - k]

                # Entering window
                total += nums[i + k + 1]

        return avgs