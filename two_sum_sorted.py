class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        while left<right:
            #finding sum
            sum=numbers[left]+numbers[right]
            #found case 
            if sum==target:
                return [left+1,right+1]
            #sum is less than tarhet
            elif sum<target:
                left+=1
            #sum is greater than target
            else:
                right-=1


