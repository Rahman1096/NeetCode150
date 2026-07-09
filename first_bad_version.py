# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #input range is 1 -> n
        left=1
        #creating right just for fun its not required as n can work in its place
        right=n
        while left<=right:
            mid=left+(right-left)//2
            if  (isBadVersion(mid)):
                right=mid-1
            else:
                left=mid+1              
        return left                    