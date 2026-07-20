class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
            
        # We process each factor manually one by one to avoid bracket errors
        
        # 1. Divide out all the 2s
        while n % 2 == 0:
            n = n // 2
            
        # 2. Divide out all the 3s
        while n % 3 == 0:
            n = n // 3
            
        # 3. Divide out all the 5s
        while n % 5 == 0:
            n = n // 5
                
        # If the number is crushed down to 1, it is an ugly number
        return n == 1
