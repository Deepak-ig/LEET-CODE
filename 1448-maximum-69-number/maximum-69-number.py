class Solution:
    def maximum69Number (self, num: int) -> int:
        # Step 1: Convert the number to text so we can manipulate individual characters
        num_str = str(num)
        
        # Step 2: Replace only the FIRST '6' we find with a '9'
        # The .replace(old, new, max_count) function makes this very clean
        max_str = num_str.replace('6', '9', 1)
        
        # Step 3: Convert the text back into a regular number and return it
        return int(max_str)
