class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        str_num=""
        count=0
        for num in nums:
            str_num=str(num)
            length_of_num=len(str_num)
            if length_of_num%2==0:
                count +=1
        return count        