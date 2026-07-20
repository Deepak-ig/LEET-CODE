class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        # Step 1: Create an empty list to store our shuffled result
        result = []
        
        # Step 2: Loop through the indices from 0 to n-1
        for i in range(n):
            # Add the element from the first half (x)
            result.append(nums[i])
            # Add the corresponding element from the second half (y)
            result.append(nums[i + n])
            
        # Step 3: Return the shuffled list
        return result
