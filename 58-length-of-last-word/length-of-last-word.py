class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 1. Split the string into a list of words
        words = s.split()
        
        # 2. Grab the last word from the list
        last_word = words[-1]
        
        # 3. Return how many letters are in it
        return len(last_word)
