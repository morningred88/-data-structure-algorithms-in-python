"""
Question 2: Palindrome problem
A palindrome is a string that reads the same forward and backward.
For example: radar or madam

The task is to design an optimal algorithm for checking whether a given string is palindrome or not.

"""


def checkPalindrom(s):
    # Reverse the string
    s_reverse = s[::-1]
    if s == s_reverse:
        return True
    return False


if __name__ == '__main__':
    testWord1 = 'radar'
    print(checkPalindrom(testWord1))

    testWord2 = 'car'
    print(checkPalindrom(testWord2))
