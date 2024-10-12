class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        clean_s = s.strip().split()
        return len(clean_s[-1])