class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        # Sort the array to find positions
        sorted_nums = sorted(nums)
        mapping = {}
        
        # The index of the first occurrence of a number equals the count of smaller numbers
        for i, num in enumerate(sorted_nums):
            if num not in mapping:
                mapping[num] = i
                
        # Reconstruct the result based on the original array ordering
        return [mapping[num] for num in nums]
