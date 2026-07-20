class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        # Handle cases where k is larger than the array length
        k = k % n
        
        # Helper function to reverse a section of the list in-place
        def reverse_segment(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 1: Reverse the entire array
        reverse_segment(0, n - 1)
        
        # Step 2: Reverse the first k elements
        reverse_segment(0, k - 1)
        
        # Step 3: Reverse the remaining elements
        reverse_segment(k, n - 1)
