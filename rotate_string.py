class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        original = s

        for i in range(len(s)):
            rotated = original[i:] + original[:i]
            if rotated == goal:
                return True

        return False