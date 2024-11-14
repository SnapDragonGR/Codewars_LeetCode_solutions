class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_range = set([i for i in range(max(nums) + 1)])
        number_set = num_range.difference(nums)
        number = next(iter(number_set)) if number_set else max(nums) + 1
        return number