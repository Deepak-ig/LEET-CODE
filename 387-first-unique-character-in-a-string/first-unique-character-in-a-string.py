class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Count the frequency of every character
        counts = {}
        for char in s:
            if char in counts:
                counts[char] = counts[char] + 1
            else:
                counts[char] = 1
                
        # Step 2: Find the first character that has a count of exactly 1
        for i in range(len(s)):
            char = s[i]
            if counts[char] == 1:
                return i # Return its index immediately
                
        # Step 3: If no character is unique, return -1
        return -1
