class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        freq = {}

        while n > 0:
            digit = n % 10
            freq[digit] = freq.get(digit, 0) + 1
            n //= 10

        occurence = float('inf')
        least_num = 0

        for key, value in freq.items():
            if value < occurence or (value == occurence and key < least_num):
                occurence = value
                least_num = key

        return least_num