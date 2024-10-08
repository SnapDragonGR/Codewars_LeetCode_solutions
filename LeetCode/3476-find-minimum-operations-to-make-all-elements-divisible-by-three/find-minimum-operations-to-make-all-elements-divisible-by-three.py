from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        op_count = 0
        for num in nums:
            remainder = num % 3
        
            if remainder != 0:
                op_count += 1
            
                if remainder == 2:
                    op_count += 0
                
        return op_count
        