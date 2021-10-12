"""
Variation problem 3:
Given an array A of n objects with Boolean-valued key, reorder the array so that all objects false appear first. Use O(1) additional space and O(N) time.
"""
from typing import List


def rearrange_boolean_array(A:List[bool]) -> List:

    # Initialize the placement position (index) of the 2 subarrays
    false, true = 0, len(A)
    while false < true:
        if A[false]:
            true -= 1
            A[true], A[false] = A[false], A[true]
        else:
            false += 1
    return A


array = [False, True, True, False]
print(rearrange_boolean_array(array))