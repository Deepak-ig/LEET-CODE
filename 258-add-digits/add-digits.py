class Solution:
    def addDigits(self, num: int) -> int:
        # Loop as long as the number has 2 or more digits
        while num >= 10:
            digit_sum = 0
            # Look at each digit by converting the number to text
            for char in str(num):
                digit_sum = digit_sum + int(char)
            # Update num to be the new sum and repeat
            num = digit_sum
            
        return num
