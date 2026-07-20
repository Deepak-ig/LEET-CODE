class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Step 1: Sort the numbers in order
        nums.sort()
        
        # Step 2: Return the middle element
        return nums[len(nums) // 2]
