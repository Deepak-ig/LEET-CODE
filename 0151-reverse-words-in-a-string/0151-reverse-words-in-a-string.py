class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. Split the string into a list of words (automatically removes extra spaces)
        words = s.split()
        
        # 2. Reverse the list of words
        reversed_words = words[::-1]
        
        # 3. Join the words back together with a single space
        return " ".join(reversed_words)
