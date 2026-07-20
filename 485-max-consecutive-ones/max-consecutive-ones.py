class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num == 1:
                current_count += 1
            else:
                # Update max_count and reset the current streak
                if current_count > max_count:
                    max_count = current_count
                current_count = 0
                
        # Final check in case the array ends with a streak of 1s
        return max(max_count, current_count)
