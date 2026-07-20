class Solution:
    def reverse(self, x: int) -> int:
        # 1. Reverse the number using simple string trick
        s = str(abs(x))
        reversed_str = s[::-1]
        res = int(reversed_str)
        
        # 2. Put the negative sign back if original x was negative
        if x < 0:
            res = -res
            
        # 3. If the answer is too big for 32-bit, return 0
        if res < -2147483648 or res > 2147483647:
            return 0
            
        return res
