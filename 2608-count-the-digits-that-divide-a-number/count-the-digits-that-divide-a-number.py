class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        
        # Every line inside the function must be indented 8 spaces
        for char in str(num):
            digit = int(char)
            
            if num % digit == 0:
                count = count + 1
                
        return count
