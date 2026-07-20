class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Step 1: Create two dictionaries to remember our character pairs
        s_to_t = {}
        t_to_s = {}
        
        # Step 2: Look at every character side-by-side using their position (index)
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            # Check the map from s -> t
            if char_s in s_to_t:
                # If we saw this letter before, it MUST map to the same letter
                if s_to_t[char_s] != char_t:
                    return False
            else:
                # If it is new, write down the relationship
                s_to_t[char_s] = char_t
                
            # Check the map from t -> s (To make sure no two letters share the same partner)
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s
                
        # If the loop finishes without breaking the rules, it is a perfect match!
        return True
