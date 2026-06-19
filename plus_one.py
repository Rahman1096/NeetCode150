class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num = ""

        for digit in digits:
            str_num += str(digit)

        large_number = int(str_num) + 1

        return [int(ch) for ch in str(large_number)]