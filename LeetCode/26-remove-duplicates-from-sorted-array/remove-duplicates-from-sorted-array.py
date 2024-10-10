class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = []
        for num in nums:
            if num not in new_list:
                new_list.append(num)
        
        k = len(new_list)

        for i in range(k):
            nums[i] = new_list[i]
        for i in range(k, len(nums)):
            nums[i] = '_'
        
        return k

            