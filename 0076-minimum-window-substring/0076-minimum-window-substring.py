from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        
        t_count = Counter(t)
        window_count = Counter()
        
        left = 0
        min_len = float('inf')
        ans = ""
        
        # 1. Expand the window to the right
        for right in range(len(s)):
            window_count[s[right]] += 1
            
            # 2. Check if the window has all needed letters
            # (all keys in t_count must have enough counts in window_count)
            while all(window_count[c] >= t_count[c] for c in t_count):
                # Save the smallest valid string we find
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    ans = s[left:right+1]
                
                # 3. Shrink the window from the left
                window_count[s[left]] -= 1
                left += 1
                
        return ans
