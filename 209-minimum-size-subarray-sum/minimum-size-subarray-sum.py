class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # Start with a length bigger than the whole array
        min_length = len(nums) + 1
        current_sum = 0
        left = 0
        
        # Step 1: Expand the window by adding numbers on the right
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Step 2: Once we reach the target, shrink the window from the left
            while current_sum >= target:
                # Calculate current window size
                size = right - left + 1
                
                # Save the smallest size we've seen so far
                if size < min_length:
                    min_length = size
                    
                # Subtract the left number and slide the window forward
                current_sum -= nums[left]
                left += 1
                
        # Step 3: If min_length never changed, no valid subarray was found
        if min_length > len(nums):
            return 0
        else:
            return min_length
