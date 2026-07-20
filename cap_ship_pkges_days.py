import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=1
        right=max(weights)
        while left<=right:
            mid=left +(right-left)//2
            total_days=0
            total_weight=0
            for weight in weights:
                if total_weight+weight>mid:
                    total_days +=1
                else:
                    total_weight +=weight
            if total_days>days:
                left=mid+1
            else:
                right=mid-1
        return left                    
