class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []
        s_len = len(s)
        p_len = len(p)
        
        # Sort p once at the start so we have a standard target to compare against
        target = sorted(p)
        
        # Loop through string s up to the point where string p can still fit
        for i in range(s_len - p_len + 1):
            # Take a slice of string s equal to the length of p
            window = s[i : i + p_len]
            
            # Sort the slice and check if it matches our target
            if sorted(window) == target:
                result.append(i)
                
        return result
