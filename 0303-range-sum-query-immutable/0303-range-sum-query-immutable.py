class NumArray:

    def __init__(self, nums: list[int]):
        # Create a prefix sum array starting with a 0 base case
        self.prefix_sums = [0]
        current_running_sum = 0
        
        # Calculate and store the running total up to each index
        for num in nums:
            current_running_sum += num
            self.prefix_sums.append(current_running_sum)

    def sumRange(self, left: int, right: int) -> int:
        # Subtract the running total BEFORE the left index from the total at the right index
        return self.prefix_sums[right + 1] - self.prefix_sums[left]
