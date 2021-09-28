class FactorialUsingLoop:
    """
    This class demonstrates the factorial of a given number using loop
        """

    def fact(self, n):
        fact=1
        for i in range(1, n+1):
            fact= fact*i
        return fact

factorial = FactorialUsingLoop()
factorial.fact(5)

