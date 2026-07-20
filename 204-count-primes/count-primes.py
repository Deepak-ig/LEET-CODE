class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
            
        # 1. Assume all numbers from 0 to n-1 are prime
        primes = [True] * n
        primes[0] = primes[1] = False # 0 and 1 are not prime
        
        # 2. Cross out multiples of each prime number
        for i in range(2, n):
            if primes[i]:
                # Cross out all multiples of i starting from 2 * i up to n
                for j in range(2 * i, n, i):
                    primes[j] = False
                    
        # 3. Count how many True values are left
        return sum(primes)
