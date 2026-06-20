class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = ""
        count_to_remove=0
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        left, right = 0, len(cleaned) - 1

        while left < right:

            if cleaned[left] != cleaned[right]:
                count_to_remove +=1
                if count_to_remove >1:
                    return False

            left += 1
            right -= 1
        return True