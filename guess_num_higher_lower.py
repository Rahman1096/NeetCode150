# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left=1
        right=n
        while left<=right:
            mid=left+(right-left)//2
            result=guess(mid)
            #Guess correctly
            if result==0:
                return mid
            #guess > actual number 
            elif result==-1:
            #guess is higher num
                right=mid-1
            else:
                left=mid+1


