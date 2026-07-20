class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Calculate the sum of the first window of size k
        current_window_sum = sum(nums[:k])
        max_sum = current_window_sum
        
        # Slide the window across the rest of the array
        for i in range(k, len(nums)):
            # Add the next element, subtract the element leaving the window
            current_window_sum += nums[i] - nums[i - k]
            if current_window_sum > max_sum:
                max_sum = current_window_sum
                
        # Return the maximum average
        return max_sum / k
