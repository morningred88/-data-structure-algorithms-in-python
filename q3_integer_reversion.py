"""
Question 3: Integer reversion 
Design an efficient algorithm to reverse a given integer. 
For example, if the input if the algorithm is 1234, then the output should be 4321.

"""


def reverseInteger(int):
    reversedInteger = 0
    while int > 0:
        remainder = 0
        remainder = int % 10
        # integer devision
        int = int//10
        reversedInteger = reversedInteger*10 + remainder
    return reversedInteger


if __name__ == '__main__':
    print(reverseInteger(12034))
