class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Define the search range
        left = 1
        right = num
        
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == num:
                return True # We found the exact square root
            elif square < num:
                left = mid + 1 # Our guess was too small, look in the right half
            else:
                right = mid - 1 # Our guess was too big, look in the left half
                
        return False # The loop finished and no perfect square was found
