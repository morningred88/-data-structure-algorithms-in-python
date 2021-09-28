class CumulativeSum:
    """
    Example problem 1
    Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer
    For example, if n=4, return 4=3=2=1=0, which is 10
    """

    def rec_sum(self, n):
        if n == 0:
            return 0
        else:
            return n + self.rec_sum(n - 1)


cumulative = CumulativeSum()
cumulative.rec_sum(4)
