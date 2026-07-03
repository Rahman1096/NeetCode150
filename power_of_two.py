class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        if n%2!=0:
            return False
        #Starting number
        i=2
        while n>0:
            n //=i
            if n%2 !=0:
                return False

        return n==1