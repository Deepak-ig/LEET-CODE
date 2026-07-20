class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # n must be greater than 0, and have exactly one set bit
        return n > 0 and (n & (n - 1)) == 0

