class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)

        sum_int = a + b

        return bin(sum_int)[2:]