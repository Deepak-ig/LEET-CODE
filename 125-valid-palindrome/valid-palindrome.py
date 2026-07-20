class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Keep only letters and numbers, and make them lowercase
        cleaned = [char.lower() for char in s if char.isalnum()]
        
        # Step 2: Check if the cleaned list reads the same forward and backward
        return cleaned == cleaned[::-1]
