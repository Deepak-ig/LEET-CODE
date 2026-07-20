class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Create a set of vowels for fast lookups
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        current_vowels = 0
        
        # 1. Count the vowels in the very first window of size k
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
                
        max_vowels = current_vowels
        
        # 2. Slide the window across the rest of the string
        for i in range(k, len(s)):
            # Add the new character entering the window on the right
            if s[i] in vowels:
                current_vowels += 1
                
            # Remove the old character leaving the window on the left
            if s[i - k] in vowels:
                current_vowels -= 1
                
            # Keep track of the highest count we've seen
            if current_vowels > max_vowels:
                max_vowels = current_vowels
                
        return max_vowels
