class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left=1
        right=x//2  #optimization as sqrt(x)<=x/2 for x >2
        while left<=right:
            mid=left+(right-left)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                right=mid-1
            else:
                left=mid+1
        return right     
        