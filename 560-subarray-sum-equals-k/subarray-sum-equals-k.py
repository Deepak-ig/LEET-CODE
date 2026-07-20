class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # A dictionary to remember how many times we've seen certain prefix sums
        prefix_counts = {0: 1}
        
        current_sum = 0
        total_answers = 0
        
        for num in nums:
            # 1. Add the current number to our running total
            current_sum = current_sum + num
            
            # 2. Check if we have seen a past sum that creates a gap of 'k'
            goal = current_sum - k
            if goal in prefix_counts:
                total_answers = total_answers + prefix_counts[goal]
                
            # 3. Add our new current_sum to the dictionary so future loops can see it
            if current_sum in prefix_counts:
                prefix_counts[current_sum] = prefix_counts[current_sum] + 1
            else:
                prefix_counts[current_sum] = 1
                
        return total_answers
