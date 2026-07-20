class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # Step 1: Square every number in the array
        squared_nums = [x * x for x in nums]
        
        # Step 2: Sort the squared numbers from smallest to largest
        squared_nums.sort()
        
        # Step 3: Return the sorted list
        return squared_nums
