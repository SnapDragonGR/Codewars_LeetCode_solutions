class Solution:
    def hammingWeight(self, n: int) -> int:
        n_bin = bin(n)[2:]
        bit_count = 0
        for digit in str(n_bin):
            if digit == "1":
                bit_count += 1
        return bit_count

