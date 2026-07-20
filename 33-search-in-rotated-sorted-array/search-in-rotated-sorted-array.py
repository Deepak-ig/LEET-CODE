class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Step 1: Find where the array was rotated (the smallest number's index)
        min_index = nums.index(min(nums))
        
        # Step 2: Set up our pointers for the whole array
        left = 0
        right = len(nums) - 1
        
        # Step 3: Do a regular, standard binary search
        while left <= right:
            mid = (left + right) // 2
            
            # Since the array is rotated, we must calculate the "real" middle index
            real_mid = (mid + min_index) % len(nums)
            
            # Check if we found the target
            if nums[real_mid] == target:
                return real_mid
                
            # If the number is too small, look in the right half
            if nums[real_mid] < target:
                left = mid + 1
            # If the number is too big, look in the left half
            else:
                right = mid - 1
                
        # Target not found
        return -1
