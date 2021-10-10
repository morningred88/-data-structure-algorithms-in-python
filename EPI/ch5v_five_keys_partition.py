"""
My own question to variation question 2
Given an array A of n objects with keys that takes one of five values, reorder the arrays so that all objects that have the same key appear together. Use O(1) space and O(n) time

This question is used to prove the explanation I wrote for partition problems in variation question 2
"""
from typing import List


def five_keys_partition(A:List[int], first: int, second: int, third: int, fourth: int, fifth: int)-> List:

    first_key, second_key, third_key, fourth_key, fifth_key = 0, 0, 0, 0, len(A)

    while fourth_key < fifth_key:
        if A[fourth_key] == first:
            A[first_key], A[fourth_key] = A[fourth_key], A[first_key]
            A[fourth_key], A[second_key] = A[second_key], A[fourth_key]
            A[fourth_key], A[third_key] = A[third_key], A[fourth_key]
            first_key, second_key, third_key, fourth_key = first_key +1, second_key +1, third_key +1, fourth_key+1
        elif A[fourth_key] == second:
            A[second_key], A[fourth_key] = A[fourth_key], A[second_key]
            A[fourth_key], A[third_key] = A[third_key], A[fourth_key]
            second_key, third_key, fourth_key = second_key + 1, third_key + 1, fourth_key+1
        elif A[fourth_key] == third:
            A[fourth_key], A[third_key] = A[third_key], A[fourth_key]
            third_key, fourth_key = third_key + 1, fourth_key+1
        elif A[fourth_key] == fourth:
            fourth_key += 1
        else:
            # A[fifth_key] == fifth
            fifth_key -= 1
            A[fourth_key], A[fifth_key] =A[fifth_key], A[fourth_key]

    return A


array = [2, 1, 1, 2, 4, 3, 5, 1, 2, 5, 1, 2, 4, 2, 3]
print(five_keys_partition(array, 1, 2, 3, 4, 5))

