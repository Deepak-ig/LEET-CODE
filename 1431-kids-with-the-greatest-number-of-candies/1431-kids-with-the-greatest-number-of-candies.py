class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # Step 1: Find the current maximum candies among all kids
        max_candies = max(candies)
        
        # Step 2: Check if each kid's candies + extraCandies >= max_candies
        return [kid_candies + extraCandies >= max_candies for kid_candies in candies]
