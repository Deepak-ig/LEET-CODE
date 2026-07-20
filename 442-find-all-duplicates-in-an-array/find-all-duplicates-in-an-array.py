class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        # Step 1: Create a tally sheet list to count how many times we see each number
        # We make it size n + 1 so the index numbers match our array numbers exactly
        counts = [0] * (len(nums) + 1)
        
        # Step 2: Count how many times each number appears
        for num in nums:
            counts[num] += 1
            
        # Step 3: Find the numbers that have a count of exactly 2
        duplicates = []
        for i in range(len(counts)):
            if counts[i] == 2:
                duplicates.append(i)
                
        return duplicates
