class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import Counter

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        counts = Counter(nums)
        # Sum keys where the value (frequency) is exactly 1
        return sum(num for num, count in counts.items() if count == 1)
