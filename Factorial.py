class FactorialUsingRecursion:
    """
    This class demonstrate the factorial of a given number using recursion
    """

    def fact(self, number):

        # Base case
        if number == 0:
            return 1
        else:
            return number * self.fact(number-1)


factorial = Factorial()
print(factorial.fact(5))

