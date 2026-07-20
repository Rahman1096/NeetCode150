import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left<=right:
            mid=left + (right-left)//2
            req_hour_at_mid=0
            for bananas in piles:
                req_hour_at_mid +=math.ceil(bananas/mid)
            if req_hour_at_mid>h:
                left=mid+1
            else:
                right=mid-1


        return left            