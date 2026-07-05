class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Stack to store all valid scores
        scores = []

        for op in operations:

            # Add the sum of the last two valid scores
            if op == '+':
                scores.append(scores[-1] + scores[-2])

            # Add double of the previous valid score
            elif op == 'D':
                scores.append(scores[-1] * 2)

            # Remove the previous valid score
            elif op == 'C':
                scores.pop()

            # Current operation is an integer score
            else:
                scores.append(int(op))

        # Return the total score
        return sum(scores)