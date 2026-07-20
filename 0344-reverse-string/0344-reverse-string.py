class Solution:
    def reverseString(self, s: list[str]) -> None:
        # Set up pointers at the very beginning and the very end
        left = 0
        right = len(s) - 1
        
        # Swap characters until pointers meet in the middle
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
