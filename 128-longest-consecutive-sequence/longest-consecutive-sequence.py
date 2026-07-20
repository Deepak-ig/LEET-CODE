class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # 1. Put all numbers into a set for instant O(1) lookups
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # 2. Check if 'num' is the START of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1
                
                # 3. Count how far the sequence goes
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                    
                # 4. Keep the highest record
                if current_streak > longest_streak:
                    longest_streak = current_streak
                    
        return longest_streak
