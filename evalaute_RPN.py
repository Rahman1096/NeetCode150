class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ch in tokens:
            if ch in '+*/-':
                op1=stack.pop()
                op2=stack.pop()
                answer=None
                if ch=='+':
                    answer=op2+op1
                elif ch=='-':
                    answer=op2-op1
                elif ch=='*':
                    answer=op2*op1
                elif ch=='/':
                    answer=int(op2/op1)
                stack.append(answer)  
            else:
                stack.append(int(ch))  
        return stack[0]                     