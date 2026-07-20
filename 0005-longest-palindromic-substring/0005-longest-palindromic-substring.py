class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
            
        start = 0
        end = 0
        
        # Helper function to find the length of a palindrome around a center
        def expandAroundCenter(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            # Check for odd-length palindromes (single character center)
            len1 = expandAroundCenter(i, i)
            # Check for even-length palindromes (two character center)
            len2 = expandAroundCenter(i, i + 1)
            
            # Find the maximum length between the two
            max_len = max(len1, len2)
            
            # If we found a longer palindrome, update our start and end indices
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]
