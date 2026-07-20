class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        left = 0
        max_freq = 0  # Tracks the frequency of the most common character in the CURRENT window
        
        for right in range(len(s)):
            # 1. Add the character to our frequency map
            char = s[right]
            count[char] = count.get(char, 0) + 1
            
            # 2. Update the highest frequency of any single character in our window
            if count[char] > max_freq:
                max_freq = count[char]
                
            # 3. Calculate how many replacements we need
            window_len = right - left + 1
            replacements_needed = window_len - max_freq
            
            # 4. If we need more than k replacements, shrink the window from the left
            if replacements_needed > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1
                
            # 5. Update our longest valid substring record
            current_window_len = right - left + 1
            if current_window_len > max_length:
                max_length = current_window_len
                
        return max_length
