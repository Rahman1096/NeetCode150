class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count_operation=0
        while num1!=0 and num2!=0:
            count_operation +=1
            if num1>num2:
                num1= num1-num2
            else:
                num2= num2-num1
        return count_operation