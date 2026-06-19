from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for entry in freq.values():
            if entry >1:
                return True
        return False             