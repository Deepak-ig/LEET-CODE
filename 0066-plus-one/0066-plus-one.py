class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Start looking from the last digit backwards to the first
        for i in range(len(digits) - 1, -1, -1):
            # If the digit is less than 9, just add 1 and return immediately
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0 (and the loop carries 1 over to the next index)
            digits[i] = 0
            
        # If the loop finishes, it means all digits were 9s (e.g., [9, 9, 9] became)
        # We must insert a new 1 at the very front
        return [1] + digits
