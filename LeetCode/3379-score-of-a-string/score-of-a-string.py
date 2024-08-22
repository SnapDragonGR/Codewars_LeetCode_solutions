class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for character in range(len(s) - 1):
            ascii_value_current = ord(s[character])
            ascii_value_next = ord(s[character + 1])

            score += abs(ascii_value_current - ascii_value_next)
        
        return score
        

        