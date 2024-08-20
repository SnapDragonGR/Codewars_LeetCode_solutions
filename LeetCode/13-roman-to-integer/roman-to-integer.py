class Solution:
    def romanToInt(self, s: str) -> int:
        rom_to_arab = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    
        i = 0
        tot = 0

        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in rom_to_arab:
                tot += rom_to_arab[s[i:i+2]]
                i += 2
            else:
                tot += rom_to_arab[s[i]]
                i += 1
        return tot