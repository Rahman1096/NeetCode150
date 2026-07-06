class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Stores indices of elements that are waiting
        stack = []

        # Initially, assume no next greater element exists
        answer = [-1] * n

        # Traverse the array twice to simulate a circular array
        for i in range(2 * n):

            # Convert i into a valid index
            index = i % n

            # Current element satisfies all smaller waiting elements
            while stack and nums[index] > nums[stack[-1]]:
                waiting = stack.pop()
                answer[waiting] = nums[index]

            # Push indices only during the first traversal
            # During the second traversal, we only help waiting elements
            if i < n:
                stack.append(index)
        return answer