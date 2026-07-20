class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 1. Count how many white 'W' blocks are in the very first window of size k
        white_count = 0
        for i in range(k):
            if blocks[i] == 'W':
                white_count += 1
                
        min_operations = white_count
        
        # 2. Slide the window one block at a time across the rest of the string
        for i in range(k, len(blocks)):
            # If the new block entering the window on the right is 'W', add 1 to our count
            if blocks[i] == 'W':
                white_count += 1
                
            # If the old block leaving the window on the left was 'W', subtract 1 from our count
            if blocks[i - k] == 'W':
                white_count -= 1
                
            # Keep track of the lowest number of 'W's we have seen in any window
            if white_count < min_operations:
                min_operations = white_count
                
        return min_operations
