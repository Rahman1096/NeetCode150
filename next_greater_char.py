class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # This letter could be the answer,
            # but there might be a smaller valid one on the left.
            if letters[mid] > target:
                right = mid - 1

            # This letter cannot be the answer.
            # It is either smaller than or equal to the target.
            else:
                left = mid + 1

        # No greater letter exists, so wrap around.
        if left == len(letters):
            return letters[0]

        return letters[left]