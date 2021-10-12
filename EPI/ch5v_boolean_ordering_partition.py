"""
Variation problem 4:
Given an array A of n objects with Boolean-valued key, reorder the array so that all objects false appear first.
The relative ordering of key true should not be change.
Use O(1) additional space and O(N) time.
"""

from typing import List


def rearrange_boolean_ordering(A:List[bool]) -> List:

    # Initialize the placement position (index) of the 2 subarrays
    false, true = 0, 0
    for i in range(len(A)):
        if A[i]:
            true += 1
        else:
            A[true], A[false] = A[false], A[true]
            false, true = false + 1, true + 1

    return A


array = [False, True, True, False]
print(rearrange_boolean_ordering(array))