"""
Variation question 2
Given an array A of n objects with keys that takes one of four values, reorder the arrays so that all objects that have the same key appear together. Use O(1) space and O(n) time
"""

from typing import List

def four_keys_partition(A:List[int], first: int, second: int, third: int, forth: int)-> List:

    first_key, second_key, third_key, forth_key = 0, 0, 0, len(A)

    while (third_key < forth_key):
        if A[third_key] == first:
            A[first_key], A[third_key] = A[third_key], A[first_key]
            A[third_key], A[second_key] = A[second_key], A[third_key]
            first_key, second_key, third_key = first_key +1, second_key +1, third_key +1

        elif A[third_key] == second:
            A[second_key], A[third_key] = A[third_key], A[second_key]
            second_key, third_key = second_key + 1, third_key + 1
        elif A[third_key] == third:
            third_key +=1
        else:
            forth_key -=1
            A[forth_key], A[third_key] =A[third_key], A[forth_key]

    return A

print(four_keys_partition([2, 1, 1, 2, 4, 3, 1, 2, 3, 1, 2, 4, 2, 3], 1, 2, 3, 4))

