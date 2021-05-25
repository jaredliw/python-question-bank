from functools import reduce  # Remove this line in python 2
from math import factorial


class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime: 20 ms
        # Memory: 13.7 MB
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        
        prime_count = 0
        for p in primes:
            if p <= n:
                prime_count += 1
            else:
                break
        
        return (factorial(prime_count) * factorial(n - prime_count)) % 1000000007