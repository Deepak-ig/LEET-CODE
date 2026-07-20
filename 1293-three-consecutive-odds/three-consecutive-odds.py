class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        consecutive_odds = 0
        
        for num in arr:
            # Check if the number is odd using bitwise AND or modulo
            if num & 1:  # Equivalent to num % 2 != 0
                consecutive_odds += 1
                if consecutive_odds == 3:
                    return True
            else:
                consecutive_odds = 0  # Reset the streak if an even number is seen
                
        return False
