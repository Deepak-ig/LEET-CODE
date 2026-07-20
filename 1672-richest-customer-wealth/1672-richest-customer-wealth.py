class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        # Calculate the total sum of each customer's row, then pick the maximum value
        return max(sum(customer) for customer in accounts)
