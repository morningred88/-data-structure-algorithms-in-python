class DigitsSum:
    """
    Example problem 2
    Given an integer, create a function which return the sum of all the individual digits in that integer.
    For example: if n=4321, return 4+3+2+1
    """

    def rec_sum(self, n):

        # Base case
        if n < 10:
            return n
        else:
            return n % 10 + self.rec_sum(int(n / 10))


digitsSum = DigitsSum()
print(digitsSum.rec_sum(4321))
