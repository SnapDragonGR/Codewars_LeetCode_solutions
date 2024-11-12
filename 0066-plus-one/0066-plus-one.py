class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int(''.join(str(digit) for digit in digits))
        digits += 1
        return [int(i) for i in str(digits)]
        