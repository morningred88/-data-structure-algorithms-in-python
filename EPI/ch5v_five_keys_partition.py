"""
My own question to variation question 2
Given an array A of n objects with keys that takes one of five values, reorder the arrays so that all objects that have the same key appear together. Use O(1) space and O(n) time

This question is used to prove the explanation I wrote for partition problems in variation question 2
"""
from typing import List


def five_keys_partition(A:List[int], first_key: int, second_key: int, third_key: int, fourth_key: int, fifth_key: int) -> List:

    first, second, third, fourth, fifth_key = 0, 0, 0, 0, len(A)

    while fourth < fifth_key:
        if A[fourth] == first_key:
            A[first], A[fourth] = A[fourth], A[first]
            A[fourth], A[second] = A[second], A[fourth]
            A[fourth], A[third] = A[third], A[fourth]
            first, second, third, fourth = first +1, second +1, third +1, fourth+1
        elif A[fourth] == second_key:
            A[second], A[fourth] = A[fourth], A[second]
            A[fourth], A[third] = A[third], A[fourth]
            second, third, fourth = second + 1, third + 1, fourth+1
        elif A[fourth] == third_key:
            A[fourth], A[third] = A[third], A[fourth]
            third, fourth = third + 1, fourth+1
        elif A[fourth] == fourth_key:
            fourth += 1
        else:
            # A[fifth_key] == fifth
            fifth_key -= 1
            A[fourth], A[fifth_key] =A[fifth_key], A[fourth]

    return A


array = [2, 1, 1, 2, 4, 3, 5, 1, 2, 5, 1, 2, 4, 2, 3]
print(five_keys_partition(array, 1, 2, 3, 4, 5))

