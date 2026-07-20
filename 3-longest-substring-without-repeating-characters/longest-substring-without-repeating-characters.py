class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = {}
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            
            # If the character is already inside the current window,
            # jump the left pointer right past its previous location
            if char in seen_chars and seen_chars[char] >= left:
                left = seen_chars[char] + 1
                
            # Update the character's newest position
            seen_chars[char] = right
            
            # Calculate the current window size and track the maximum
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                
        return max_length
