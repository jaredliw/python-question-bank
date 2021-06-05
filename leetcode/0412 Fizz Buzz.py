class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Python 2:
        # Runtime: 24 ms
        # Memory: 14.1 MB

        # Python 3:
        # Runtime: 40s
        # Memory: 14.8 MB
        return map(lambda x: "FizzBuzz" if not x % 15 else "Buzz" if not x % 5 else "Fizz" if not x % 3 else str(x),
                   range(1, n + 1))
