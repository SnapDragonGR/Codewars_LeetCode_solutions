from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []

        for number in candies:
            result.append((number + extraCandies) >= max_candies)

        return result
        