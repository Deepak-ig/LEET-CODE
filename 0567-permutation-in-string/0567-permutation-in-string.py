class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        
        # Sort s1 once at the start so we have a target to compare against
        target = sorted(s1)
        
        # Loop through string s2 up to the point where s1 can still fit
        for i in range(len2 - len1 + 1):
            # Cut out a window from s2 equal to the length of s1
            window = s2[i : i + len1]
            
            # Sort the window. If it matches our target, we found a permutation!
            if sorted(window) == target:
                return True
                
        return False
