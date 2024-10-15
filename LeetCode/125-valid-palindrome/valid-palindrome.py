import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(' ', '')
        clean_s = ''
        for char in s:
            if char not in string.punctuation:
                clean_s += char
        
        if clean_s == clean_s[::-1]:
            return True
        else:
            return False