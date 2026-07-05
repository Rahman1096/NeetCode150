class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s=[]
        stack_t=[]
        #doing operation on each string seprately. we can do using a single loop as well 
        for ch in s:
            if stack_s and ch=="#":
                stack_s.pop()
            elif not stack_s and ch=='#':
                continue
            else:
                stack_s.append(ch)
        #for 2nd string t         
        for ch in t:
            if stack_t and ch=="#":
                stack_t.pop()
            elif not stack_t and  ch=='#':
                continue    
            else:
                stack_t.append(ch)

        return stack_s==stack_t 