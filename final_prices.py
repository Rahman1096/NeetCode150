class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        # Initially, everyone pays the original price
        answer = prices[:]

        for i in range(len(prices)):

            # Current price cannot give discount
            if not stack or prices[stack[-1]] < prices[i]:
                stack.append(i)

            else:
                # Current price gives discount to all larger waiting prices
                while stack and prices[stack[-1]] >= prices[i]:
                    waiting = stack.pop()
                    answer[waiting] = prices[waiting] - prices[i]

                # Current price now starts waiting
                stack.append(i)

        return answer