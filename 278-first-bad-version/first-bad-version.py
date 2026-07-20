# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Define the search range: 1 to n
        left = 1
        right = n
        
        while left < right:
            mid = (left + right) // 2
            
            # If the middle version is bad, the first bad version must be at or before 'mid'
            if isBadVersion(mid):
                right = mid
            else:
                # If the middle version is good, the first bad version must be after 'mid'
                left = mid + 1
                
        # When left and right meet, we've found our first bad version
        return left
