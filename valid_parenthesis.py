class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:

            # Opening bracket
            if ch in "([{":
                stack.append(ch)

            # Closing bracket
            elif len(stack) > 0:
                top = stack[-1]

                if ch == ')' and top == '(':
                    stack.pop()
                elif ch == ']' and top == '[':
                    stack.pop()
                elif ch == '}' and top == '{':
                    stack.pop()
                else:
                    return False

            # Stack is empty
            else:
                return False

        return len(stack) == 0