class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = str(x)
        if digits == digits[::-1]:
            return True
        else:
            return False