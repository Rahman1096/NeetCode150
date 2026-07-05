class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        answer=[0]*len(temperatures)

        for i in range(len(temperatures)):
            #if stack is empty or current element is less than top of stack 
            if not stack or temperatures[i]<=temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[i]>temperatures[stack[-1]]:
                    # we pop the index of day who was waiting
                    waiting_day_index=stack.pop()
                    answer[waiting_day_index]=i-waiting_day_index
                stack.append(i)      
        return answer          
