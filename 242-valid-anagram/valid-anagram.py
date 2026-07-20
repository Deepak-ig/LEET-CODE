class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort both strings and compare them
        return sorted(s) == sorted(t)
