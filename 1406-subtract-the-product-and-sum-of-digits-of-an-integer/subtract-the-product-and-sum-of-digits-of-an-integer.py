class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Step 1: Turn the number into text and set up trackers
        digits_text = str(n)
        total_product = 1
        total_sum = 0
        
        # Step 2: Loop through each digit text character
        for char in digits_text:
            digit = int(char) # Turn it back into a number
            total_product = total_product * digit
            total_sum = total_sum + digit
            
        # Step 3: Return the final difference
        return total_product - total_sum

